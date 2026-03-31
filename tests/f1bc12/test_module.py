import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestFrontendIndex:
    
    @pytest.fixture
    def html_file_path(self):
        """获取HTML文件路径的fixture"""
        return Path(__file__).parent.parent / "frontend" / "index.html"
    
    @pytest.fixture
    def html_content(self, html_file_path):
        """读取HTML文件内容的fixture"""
        if html_file_path.exists():
            with open(html_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        return None
    
    def test_html_file_exists(self, html_file_path):
        """测试HTML文件是否存在"""
        assert html_file_path.exists(), f"HTML文件不存在: {html_file_path}"
        assert html_file_path.is_file(), f"路径不是文件: {html_file_path}"
    
    def test_html_contains_audio_elements(self, html_content):
        """测试HTML文件是否包含音效系统相关的关键元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查是否包含音频相关元素
        audio_elements = soup.find_all(['audio', 'button', 'input'])
        assert len(audio_elements) > 0, "HTML文件中未找到音频控制元素"
        
        # 检查是否包含音效系统相关的类名或ID
        audio_related_attrs = []
        for element in soup.find_all(attrs={'class': True}):
            audio_related_attrs.extend(element.get('class', []))
        for element in soup.find_all(attrs={'id': True}):
            audio_related_attrs.append(element.get('id'))
        
        audio_keywords = ['audio', 'sound', 'music', 'play', 'volume', 'control']
        has_audio_related = any(
            any(keyword in str(attr).lower() for keyword in audio_keywords)
            for attr in audio_related_attrs
        )
        assert has_audio_related, "HTML文件中未找到音效系统相关的类名或ID"
    
    def test_html_structure_validity(self, html_content):
        """测试HTML文件结构的有效性"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html') is not None, "HTML文件缺少<html>标签"
        assert soup.find('head') is not None, "HTML文件缺少<head>标签"
        assert soup.find('body') is not None, "HTML文件缺少<body>标签"
        
        # 检查title标签
        title = soup.find('title')
        assert title is not None, "HTML文件缺少<title>标签"
        assert len(title.get_text().strip()) > 0, "HTML文件的title标签为空"
        
        # 检查是否包含JavaScript或CSS引用（音效系统通常需要）
        scripts = soup.find_all('script')
        styles = soup.find_all(['style', 'link'])
        assert len(scripts) > 0 or len(styles) > 0, "HTML文件中未找到JavaScript或CSS引用"

    def test_html_contains_interactive_elements(self, html_content):
        """测试HTML文件是否包含交互式元素用于音效控制"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查交互式元素
        interactive_elements = soup.find_all(['button', 'input', 'select', 'audio'])
        assert len(interactive_elements) > 0, "HTML文件中未找到交互式元素"
        
        # 检查是否有事件处理相关的属性
        event_attrs = ['onclick', 'onchange', 'onplay', 'onpause', 'onended']
        has_events = False
        for element in soup.find_all():
            for attr in event_attrs:
                if element.get(attr):
                    has_events = True
                    break
            if has_events:
                break
        
        # 如果没有内联事件，检查是否有可能通过JavaScript绑定事件的元素
        if not has_events:
            elements_with_ids = soup.find_all(attrs={'id': True})
            elements_with_classes = soup.find_all(attrs={'class': True})
            assert len(elements_with_ids) > 0 or len(elements_with_classes) > 0, \
                "HTML文件中未找到可用于事件绑定的元素（缺少id或class属性）"