import os

# HTML টেমপ্লেট, যেখানে দুটি জায়গা পরিবর্তন হবে: {TOPIC_TITLE} এবং {PDF_FILENAME}
html_template = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <title>{TOPIC_TITLE}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ font-family: sans-serif; margin: 0; padding: 0; background-color: #f0f2f5; }}
        .container {{ max-width: 90%; margin: 20px auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 15px rgba(0,0,0,0.1); }}
        h1 {{ text-align: center; color: #333; }}
        .pdf-viewer {{ width: 100%; height: 85vh; border: 1px solid #ddd; border-radius: 5px; }}
        .back-link {{ display: block; text-align: center; margin-top: 20px; color: #3498db; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{TOPIC_TITLE}</h1>
        <iframe class="pdf-viewer" src="{PDF_FILENAME}"></iframe>
        <a class="back-link" href="../../../../index.html">← মূল সূচিপত্রে ফিরে যান</a>
    </div>
</body>
</html>
"""

# যে ফোল্ডার থেকে কাজ শুরু হবে
root_directory = 'subjects'

print("HTML ফাইল তৈরি করা শুরু হচ্ছে...")

# সমস্ত ফোল্ডার এবং সাব-ফোল্ডারের মধ্যে দিয়ে যাওয়া
for dirpath, dirnames, filenames in os.walk(root_directory):
    # যদি কোনো ফোল্ডারের ভেতরে আর কোনো ফোল্ডার না থাকে, তবে সেটিই চূড়ান্ত টপিক ফোল্ডার
    if not dirnames:
        # ফোল্ডারের নাম থেকে টপিকের শিরোনাম এবং PDF ফাইলের নাম তৈরি করা
        folder_name = os.path.basename(dirpath)
        topic_title = folder_name.replace('-', ' ').title()
        pdf_filename = folder_name + ".pdf"  # ফোল্ডারের নাম অনুযায়ী PDF-এর নাম ধরা হচ্ছে
        
        # page.html ফাইলের সম্পূর্ণ পাথ তৈরি করা
        page_html_path = os.path.join(dirpath, 'page.html')
        
        # টেমপ্লেটের মধ্যে শিরোনাম এবং PDF ফাইলের নাম বসিয়ে ফাইনাল HTML তৈরি করা
        final_html_content = html_template.format(
            TOPIC_TITLE=topic_title,
            PDF_FILENAME=pdf_filename
        )
        
        # নতুন page.html ফাইলটি লেখা
        try:
            with open(page_html_path, 'w', encoding='utf-8') as f:
                f.write(final_html_content)
            print(f"সফলভাবে তৈরি হয়েছে: {page_html_path}")
        except Exception as e:
            print(f"ত্রুটি: {page_html_path} তৈরিতে সমস্যা হয়েছে - {e}")

print("\nকাজ সম্পন্ন! সমস্ত page.html ফাইল তৈরি হয়ে গেছে।")