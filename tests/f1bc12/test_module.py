import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestIndexHTML:
    
    @pytest.fixture
    def html_file_path(self):
        """获取index.html文件路径的fixture"""
        return Path(__file__).parent.parent / "frontend" / "index.html"
    
    @pytest.fixture
    def html_content(self, html_file_path):
        """读取HTML文件内容的fixture"""
        if html_file_path.exists():
            with open(html_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        return None
    
    def test_html_file_exists(self, html_file_path):
        """测试index.html文件是否存在"""
        assert html_file_path.exists(), f"HTML文件不存在: {html_file_path}"
        assert html_file_path.is_file(), f"路径不是文件: {html_file_path}"
    
    def test_html_contains_game_elements(self, html_content):
        """测试HTML文件是否包含游戏相关的关键元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查是否包含游戏容器或画布元素
        game_container = soup.find(id='game') or soup.find(class_='game-container') or soup.find('canvas')
        assert game_container is not None, "HTML中缺少游戏容器元素（#game、.game-container或canvas）"
        
        # 检查是否包含游戏相关的关键词
        html_text = html_content.lower()
        game_keywords = ['game', 'play', 'start', 'canvas', 'score']
        found_keywords = [keyword for keyword in game_keywords if keyword in html_text]
        assert len(found_keywords) > 0, f"HTML中缺少游戏相关关键词，期望包含: {game_keywords}"
    
    def test_html_contains_pause_functionality(self, html_content):
        """测试HTML文件是否包含暂停功能相关元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        html_text = html_content.lower()
        
        # 检查暂停相关的按钮或元素
        pause_button = (soup.find('button', string=lambda text: text and 'pause' in text.lower()) or
                       soup.find(id='pause') or 
                       soup.find(class_='pause-btn') or
                       soup.find('button', {'onclick': lambda x: x and 'pause' in x.lower()}))
        
        # 或者检查是否包含暂停相关的文本内容
        pause_keywords = ['pause', 'resume', 'stop', '暂停', '继续']
        found_pause_keywords = [keyword for keyword in pause_keywords if keyword in html_text]
        
        assert pause_button is not None or len(found_pause_keywords) > 0, \
            "HTML中缺少暂停功能相关元素或关键词"
    
    def test_html_has_valid_structure(self, html_content):
        """测试HTML文件是否具有有效的基本结构"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html') is not None, "HTML文件缺少<html>标签"
        assert soup.find('head') is not None, "HTML文件缺少<head>标签"
        assert soup.find('body') is not None, "HTML文件缺少<body>标签"
        
        # 检查是否有标题
        title = soup.find('title')
        assert title is not None and title.get_text().strip(), "HTML文件缺少有效的<title>标签"
    
    def test_html_includes_javascript_or_css(self, html_content):
        """测试HTML文件是否包含JavaScript或CSS资源"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查是否包含JavaScript文件或内联脚本
        js_files = soup.find_all('script', src=True)
        inline_scripts = soup.find_all('script', src=False)
        
        # 检查是否包含CSS文件或内联样式
        css_files = soup.find_all('link', rel='stylesheet')
        inline_styles = soup.find_all('style')
        
        has_js = len(js_files) > 0 or len(inline_scripts) > 0
        has_css = len(css_files) > 0 or len(inline_styles) > 0
        
        assert has_js or has_css, "HTML文件应该包含JavaScript或CSS资源以实现游戏功能"