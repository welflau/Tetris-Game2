import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestFrontendAudioSystem:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("frontend") / "index.html"
        assert index_file.exists(), f"index.html 文件不存在: {index_file}"
        assert index_file.is_file(), f"{index_file} 不是一个有效的文件"
    
    def test_index_html_contains_audio_elements(self):
        """测试 index.html 是否包含音效系统相关的HTML元素"""
        index_file = Path("frontend") / "index.html"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否包含音频相关元素
        audio_elements = soup.find_all('audio')
        audio_controls = soup.find_all(attrs={'class': lambda x: x and 'audio' in x.lower()}) if soup.find_all(attrs={'class': True}) else []
        audio_buttons = soup.find_all('button', attrs={'class': lambda x: x and any(keyword in x.lower() for keyword in ['play', 'pause', 'stop', 'sound', 'audio']) if x else False})
        
        # 至少应该有一个音频相关元素
        total_audio_elements = len(audio_elements) + len(audio_controls) + len(audio_buttons)
        assert total_audio_elements > 0, "HTML文件中未找到音频相关元素（audio标签、音频控制按钮或音频相关class）"
    
    def test_index_html_has_basic_structure(self):
        """测试 index.html 是否具有基本的HTML结构"""
        index_file = Path("frontend") / "index.html"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html'), "HTML文件缺少html标签"
        assert soup.find('head'), "HTML文件缺少head标签"
        assert soup.find('body'), "HTML文件缺少body标签"
        
        # 检查是否有标题
        title = soup.find('title')
        assert title is not None, "HTML文件缺少title标签"
        assert len(title.get_text().strip()) > 0, "title标签内容为空"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("docs") / "f1bc12" / "0092da" / "dev-notes.md"
        assert dev_notes_file.exists(), f"开发文档文件不存在: {dev_notes_file}"
        assert dev_notes_file.is_file(), f"{dev_notes_file} 不是一个有效的文件"
    
    def test_dev_notes_contains_content(self):
        """测试开发文档是否包含有效内容"""
        dev_notes_file = Path("docs") / "f1bc12" / "0092da" / "dev-notes.md"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        assert len(content) > 0, "开发文档文件内容为空"
        
        # 检查是否包含音效系统相关关键词
        audio_keywords = ['音效', '音频', 'audio', 'sound', '播放', 'play', '系统', 'system']
        content_lower = content.lower()
        
        found_keywords = [keyword for keyword in audio_keywords if keyword.lower() in content_lower]
        assert len(found_keywords) > 0, f"开发文档中未找到音效系统相关关键词，期望包含: {audio_keywords}"
    
    def test_project_directory_structure(self):
        """测试项目目录结构是否正确"""
        frontend_dir = Path("frontend")
        docs_dir = Path("docs")
        
        assert frontend_dir.exists(), "frontend目录不存在"
        assert frontend_dir.is_dir(), "frontend不是一个目录"
        
        assert docs_dir.exists(), "docs目录不存在"
        assert docs_dir.is_dir(), "docs不是一个目录"
        
        # 检查docs子目录结构
        f1bc12_dir = docs_dir / "f1bc12"
        assert f1bc12_dir.exists(), "docs/f1bc12目录不存在"
        
        final_dir = f1bc12_dir / "0092da"
        assert final_dir.exists(), "docs/f1bc12/0092da目录不存在"