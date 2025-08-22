#!/usr/bin/env python3
"""
Script tạo HTML report đơn giản từ allure-results
"""
import os
import json
import glob
from datetime import datetime

def create_simple_report():
    """Tạo HTML report đơn giản"""
    
    print("🔍 Bắt đầu tạo report...")
    print(f"📁 Thư mục hiện tại: {os.getcwd()}")
    
    # Kiểm tra thư mục allure-results
    allure_dir = "allure-results"
    if not os.path.exists(allure_dir):
        print(f"❌ Thư mục {allure_dir} không tồn tại!")
        print("💡 Hãy chạy test trước để tạo allure-results")
        return
    
    print(f"✅ Thư mục {allure_dir} tồn tại")
    
    # Liệt kê tất cả files trong allure-results
    all_files = os.listdir(allure_dir)
    print(f"📋 Tổng số files trong {allure_dir}: {len(all_files)}")
    
    if all_files:
        print("📄 Danh sách files:")
        for file in all_files[:10]:  # Hiển thị 10 files đầu
            print(f"   - {file}")
        if len(all_files) > 10:
            print(f"   ... và {len(all_files) - 10} files khác")
    
    # Đọc tất cả result files
    result_pattern = os.path.join(allure_dir, "*-result.json")
    print(f"🔍 Tìm files với pattern: {result_pattern}")
    
    result_files = glob.glob(result_pattern)
    print(f"📊 Tìm thấy {len(result_files)} result files")
    
    if not result_files:
        print("❌ Không tìm thấy result files!")
        print("💡 Có thể test chưa được chạy hoặc allure-results trống")
        print("💡 Hãy chạy: python -m pytest test/test_login.py -v")
        return
    
    # Tạo HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Report</title>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .header {{ background: #f0f0f0; padding: 20px; border-radius: 5px; }}
            .test-case {{ margin: 10px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
            .passed {{ border-left: 5px solid #4CAF50; }}
            .failed {{ border-left: 5px solid #f44336; }}
            .screenshot {{ margin: 10px 0; }}
            .screenshot img {{ max-width: 800px; border: 1px solid #ddd; }}
            .timestamp {{ color: #666; font-size: 12px; }}
            .error {{ background: #ffebee; border-left: 5px solid #f44336; padding: 10px; margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🚀 Test Report</h1>
            <p>Generated at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <p>Total tests: {len(result_files)}</p>
            <p>Source directory: {allure_dir}</p>
        </div>
    """
    
    # Process each result file
    processed_count = 0
    error_count = 0
    passed_count = 0
    failed_count = 0
    broken_count = 0
    skipped_count = 0
    
    for result_file in result_files:
        try:
            print(f"📖 Đang xử lý: {result_file}")
            
            with open(result_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            test_name = data.get('name', 'Unknown Test')
            status = data.get('status', 'unknown')
            start_time = data.get('start', 0)
            stop_time = data.get('stop', 0)
            duration = (stop_time - start_time) / 1000 if start_time and stop_time else 0
            
            # Đếm theo status
            if status == 'passed':
                passed_count += 1
            elif status == 'failed':
                failed_count += 1
            elif status == 'broken':
                broken_count += 1
            elif status == 'skipped':
                skipped_count += 1
            
            print(f"   ✅ Test: {test_name}, Status: {status}, Duration: {duration:.2f}s")
            
            # Tìm screenshot
            screenshot_files = glob.glob(os.path.join(allure_dir, "*.png"))
            screenshot_html = ""
            for screenshot in screenshot_files:
                if test_name.lower().replace(' ', '_') in screenshot.lower():
                    screenshot_html += f'<div class="screenshot"><img src="{screenshot}" alt="Screenshot"></div>'
                    print(f"   📸 Tìm thấy screenshot: {screenshot}")
            
            # Tạo test case HTML
            status_class = "passed" if status == "passed" else "failed"
            status_icon = "✅" if status == "passed" else "❌"
            
            html_content += f"""
            <div class="test-case {status_class}">
                <h3>{status_icon} {test_name}</h3>
                <p><strong>Status:</strong> {status}</p>
                <p><strong>Duration:</strong> {duration:.2f}s</p>
                <p class="timestamp">Start: {datetime.fromtimestamp(start_time/1000).strftime('%H:%M:%S') if start_time else 'N/A'}</p>
                {screenshot_html}
            </div>
            """
            
            processed_count += 1
            
        except Exception as e:
            error_count += 1
            print(f"❌ Lỗi xử lý {result_file}: {e}")
            print(f"   🔍 Chi tiết lỗi: {type(e).__name__}: {str(e)}")
            
            # Thêm error vào HTML
            html_content += f"""
            <div class="test-case error">
                <h3>❌ Error Processing: {os.path.basename(result_file)}</h3>
                <p><strong>Error:</strong> {type(e).__name__}: {str(e)}</p>
                <p><strong>File:</strong> {result_file}</p>
            </div>
            """
    
    html_content += f"""
        <div class="header">
            <h2>📊 Summary</h2>
            <p><strong>Total Tests:</strong> {len(result_files)}</p>
            <p><strong>✅ Passed:</strong> {passed_count}</p>
            <p><strong>❌ Failed:</strong> {failed_count}</p>
            <p><strong>⚠️ Broken:</strong> {broken_count}</p>
            <p><strong>⏭️ Skipped:</strong> {skipped_count}</p>
            <p><strong>🔧 Processed:</strong> {processed_count}</p>
            <p><strong>💥 Errors:</strong> {error_count}</p>
        </div>
    </body>
    </html>
    """
    
    # Lưu HTML report
    report_file = "simple_report.html"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"\n🎉 Report đã được tạo thành công!")
    print(f"📁 File: {os.path.abspath(report_file)}")
    print(f"\n📊 THỐNG KÊ CHI TIẾT:")
    print(f"   📈 Total Tests: {len(result_files)}")
    print(f"   ✅ Passed: {passed_count}")
    print(f"   ❌ Failed: {failed_count}")
    print(f"   ⚠️ Broken: {broken_count}")
    print(f"   ⏭️ Skipped: {skipped_count}")
    print(f"   🔧 Processed: {processed_count}")
    print(f"   💥 Errors: {error_count}")
    print(f"\n💡 Mở file {report_file} trong browser để xem report")

if __name__ == "__main__":
    try:
        create_simple_report()
    except Exception as e:
        print(f"💥 Lỗi nghiêm trọng: {type(e).__name__}: {str(e)}")
        print(f"🔍 Stack trace:")
        import traceback
        traceback.print_exc()
