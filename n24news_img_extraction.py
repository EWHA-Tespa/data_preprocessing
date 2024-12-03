import json
import shutil
import os

json_file_path = 'n24news_data/news/nytimes_train.json'
base_output_dir = 'n24news/image'
image_dir = 'n24news_data/imgs'

with open(json_file_path, 'r') as file:
    data = json.load(file)

image_data = []

# image_id와 section 값을 추출
if isinstance(data, list):
    image_data = [{"image_id": item.get("image_id", ""), "section": item.get("section", "")} for item in data if "image_id" in item]
elif isinstance(data, dict) and "image_id" in data:
    image_data.append({"image_id": data.get("image_id", ""), "section": data.get("section", "")})

os.makedirs(base_output_dir, exist_ok=True)

# 디렉토리 생성 및 파일 저장
for idx, item in enumerate(image_data, start=1):
    image_id = item["image_id"]
    section = item["section"]

    dir_name = f'{base_output_dir}/image_{idx}'
    os.makedirs(dir_name, exist_ok=True)

    # image_id.txt 파일 생성
    txt_file_path = os.path.join(dir_name, "id.txt")
    with open(txt_file_path, 'w') as txt_file:
        txt_file.write(image_id)

    # section.txt 파일 생성
    section_file_path = os.path.join(dir_name, "label.txt")
    with open(section_file_path, 'w') as section_file:
        section_file.write(section)

    # 이미지 파일 복사
    image_file_path = os.path.join(image_dir, f'{image_id}.jpg')
    if os.path.exists(image_file_path):
        shutil.copy(image_file_path, dir_name)
    else:
        print(f"Image file for image_id {image_id} not found in {image_dir}")


