import sys
import io

# Force utf-8 stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('tools/local_crawler_producer.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("print(f\\\"\\\\n==================================================\\\")", "print(f\\\"\\n==================================================\\\")")
text = text.replace("print(\\\"\U0001f916", "print(\\\"")
text = text.replace("print(\\\"🚀", "print(\\\"")
text = text.replace("print(f\\\"🚀", "print(f\\\"")
text = text.replace("print(\\\"⏳", "print(\\\"")
text = text.replace("print(f\\\"⏳", "print(f\\\"")
text = text.replace("print(f\\\"✨", "print(f\\\"")
text = text.replace("print(f\\\"🎉", "print(f\\\"")
text = text.replace("print(\\\"🚀", "print(\\\"")
text = text.replace("input(", "pass # input(")

# Fix folder naming to match what we actually want or what exists
text = text.replace("dest_dir = os.path.join(CUSTOMER_DIR, f\\\"260930-{slug}\\\")", "dest_dir = os.path.join(CUSTOMER_DIR, f\\\"260930-{slug}-{clean_name}\\\")")

with open('tools/local_crawler_producer.py', 'w', encoding='utf-8') as f:
    f.write(text)

