#!/usr/bin/env python3
import re

def extract_abbr(text, entry_type=""):
    """booktitle/journal 텍스트에서 약자 추출"""
    if not text:
        return ""
    
    # 알려진 컨퍼런스/저널 매핑 (완전한 버전)
    known_abbrs = {
        # CVPR/ICCV/ECCV
        "computer vision and pattern recognition": "CVPR",
        "ieee conference on computer vision and pattern recognition": "CVPR",
        "proceedings of the ieee/cvf conference on computer vision and pattern recognition": "CVPR",
        "proceedings of the ieee conference on computer vision and pattern recognition": "CVPR",
        "proceedings of the computer vision and pattern recognition": "CVPR",
        "proceedings of the ieee/cvf international conference on computer vision": "ICCV",
        "cvf international conference on computer vision": "ICCV",
        "international conference on computer vision": "ICCV",
        "proceedings of the ieee international conference on computer vision": "ICCV",
        "european conference on computer vision": "ECCV",
        "proceedings of the european conference on computer vision": "ECCV",
        "eccv workshops": "ECCV",
        
        # Other major conferences
        "winter conference on applications of computer vision": "WACV",
        "ieee winter conference on applications": "WACV",
        "the ieee/cvf winter conference on applications": "WACV",
        "british machine vision conference": "BMVC",
        "asian conference on computer vision": "ACCV",
        "pattern recognition": "ICPR",
        "international conference on pattern recognition": "ICPR",
        
        # Robotics
        "intelligent robots and systems": "IROS",
        "ieee/rsj international conference on intelligent robots": "IROS",
        "proceedings of the ieee/rsj conference on intelligent robots": "IROS",
        "international conference on robotics and automation": "ICRA",
        "ieee international conference on robotics and automation": "ICRA",
        "ieee icra workshop": "ICRA",
        
        # 3D Vision
        "international conference on 3d vision": "3DV",
        "3dv": "3DV",
        
        # Other conferences
        "aaai conference on artificial intelligence": "AAAI",
        "proceedings of the aaai": "AAAI",
        "medical image computing and computer assisted intervention": "MICCAI",
        "international conference on medical image": "MICCAI",
        "neural information processing systems": "NeurIPS",
        "machine learning": "ICML",
        "acm international conference on multimedia": "MM",
        "proceedings of the acm international conference on multimedia": "MM",
        "multimedia expo": "ICME",
        "image processing": "ICIP",
        "circuits and systems": "ISCAS",
        "itc-cscc": "ITCCSC",
        
        # Journals
        "ieee transactions on pattern recognition and machine intelligence": "TPAMI",
        "ieee transactions on pattern analysis and machine intelligence": "TPAMI",
        "ieee transactions on image processing": "TIP",
        "ieee transactions on visualization and computer graphics": "TVCG",
        "ieee transactions on consumer electronics": "TCE",
        "ieee transactions on circuits and systems for video technology": "TCSVT",
        "ieee transactions on cognitive and developmental systems": "TCDS",
        "ieee transactions on medical imaging": "TMI",
        "ieee transactions on semiconductor manufacturing": "TSM",
        "international journal of computer vision": "IJCV",
        "computer vision and image understanding": "CVIU",
        "machine vision and applications": "MVA",
        "electronics letters": "EL",
        "applied intelligence": "AppInt",
        "proceedings of the acm on human-computer interaction": "PACM HCI",
        "proceedings of the institution of mechanical engineers": "IMechE",
        "journal of auto-vehicle safety association": "JAVSA",
        "advances in neural information processing systems": "NeurIPS",
        "arxiv": "arXiv",
        
        # Korean conferences
        "대한전기학회": "KIEE",
        "대한전자공학회": "KICE",
        "한국정보과학회": "CISK",
        "한국제어": "KICS",
        "정보 및 제어 논문집": "ICL",
        "전자공학회논문지": "JKIEE",
        "institute of electronics engineers of korea": "IEEK",
        
        # Workshops
        "workshop": "WS",
        "workshops": "WS",
        "workshop on": "WS",
        "human-robot interfaces": "HRI",
        "assistive computer vision": "ACVA",
    }
    
    text_lower = text.lower()
    
    # 정확한 매칭
    for key, val in known_abbrs.items():
        if key in text_lower:
            return val
    
    # 약자 추출 (첫 글자)
    words = re.findall(r'\b([A-Z])\w+', text)
    if words and len(words) >= 2:
        abbr = ''.join(words[:4])
        return abbr if len(abbr) <= 6 else abbr[:6]
    
    return ""

# 전체 파일 읽기
with open('/Users/hjchang/Project/cvlab-uob.github.io/_bibliography/papers.bib', 'r') as f:
    content = f.read()

# 개별 항목 분해 (@ 기호로 분리)
entries = re.split(r'(?=@)', content)

update_count = 0
new_content_parts = []

for entry in entries:
    if not entry.strip().startswith('@'):
        new_content_parts.append(entry)
        continue
    
    # entry 타입 찾기
    entry_type_match = re.search(r'@(\w+)', entry)
    entry_type = entry_type_match.group(1) if entry_type_match else ""
    
    # 각 항목에서 booktitle 또는 journal 추출
    title_match = re.search(r'booktitle\s*=\s*\{([^}]+)\}', entry)
    if not title_match:
        title_match = re.search(r'journal\s*=\s*\{([^}]+)\}', entry)
    
    venue = title_match.group(1) if title_match else ""
    abbr_val = extract_abbr(venue, entry_type)
    
    # abbr = {} 패턴이 있으면
    if 'abbr = {}' in entry:
        # venue가 없으면 entry type에 따라 기본값 설정
        if not abbr_val:
            if entry_type == "misc":
                abbr_val = "Patent"
            elif entry_type == "phdthesis":
                abbr_val = "PhD"
            else:
                abbr_val = "Preprint"
        
        entry = entry.replace('abbr = {}', f'abbr = {{{abbr_val}}}')
        update_count += 1

    new_content_parts.append(entry)

# 파일 저장
with open('/Users/hjchang/Project/cvlab-uob.github.io/_bibliography/papers.bib', 'w') as f:
    f.write(''.join(new_content_parts))

print(f"✓ papers.bib 업데이트 완료! ({update_count}개 항목 수정)")
