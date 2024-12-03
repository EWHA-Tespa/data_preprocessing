import json
import os

# JSON 파일 경로 및 출력 디렉토리 설정
json_file_path = 'n24news_data/news/nytimes_train.json'
base_output_dir = 'n24news/caption'

# JSON 파일 읽기
with open(json_file_path, 'r') as file:
    data = json.load(file)

# 데이터 추출
article_data = []
if isinstance(data, list):
    article_data = [
        {
            "article_id": item.get("article_id", ""),
            "caption": item.get("caption", ""),
            "section": item.get("section", "")  # 'section' 필드 추가
        }
        for item in data if "article_id" in item
    ]
elif isinstance(data, dict) and "article_id" in data:
    article_data.append({
        "article_id": data.get("article_id", ""),
        "caption": data.get("caption", ""),
        "section": data.get("section", "")  # 'section' 필드 추가
    })

# 출력 디렉토리 생성
os.makedirs(base_output_dir, exist_ok=True)

# 각 article_id, caption, section 저장
for idx, item in enumerate(article_data, start=1):
    article_id = item["article_id"]
    caption = item["caption"]
    section = item["section"]

    # 개별 디렉토리 생성
    dir_name = f'{base_output_dir}/caption_{idx}'
    os.makedirs(dir_name, exist_ok=True)

    # article_id.txt 생성
    article_id_path = os.path.join(dir_name, "id.txt")
    with open(article_id_path, 'w') as article_file:
        article_file.write(article_id)

    # caption.txt 생성
    caption_path = os.path.join(dir_name, "caption.txt")
    with open(caption_path, 'w') as caption_file:
        caption_file.write(caption)

    # label.txt 생성 (section 값 저장)
    label_path = os.path.join(dir_name, "label.txt")
    with open(label_path, 'w') as label_file:
        label_file.write(section)


