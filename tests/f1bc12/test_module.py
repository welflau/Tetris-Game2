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
        
        # 检查基本HTML结构
        assert soup.find('html') is not None, "缺少html标签"
        assert soup.find('head') is not None, "缺少head标签"
        assert soup.find('body') is not None, "缺少body标签"
        
        # 检查游戏相关元素
        game_keywords = ['game', 'play', 'start', 'score', 'level']
        html_lower = html_content.lower()
        
        found_keywords = [keyword for keyword in game_keywords if keyword in html_lower]
        assert len(found_keywords) > 0, f"HTML中未找到游戏相关关键词: {game_keywords}"
    
    def test_html_has_interactive_elements(self, html_content):
        """测试HTML文件是否包含交互元素如按钮、输入框或画布"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查交互元素
        buttons = soup.find_all('button')
        inputs = soup.find_all('input')
        canvas = soup.find_all('canvas')
        divs_with_onclick = soup.find_all('div', onclick=True)
        
        interactive_elements = len(buttons) + len(inputs) + len(canvas) + len(divs_with_onclick)
        
        assert interactive_elements > 0, "HTML中未找到交互元素(button、input、canvas或带onclick的div)"
    
    def test_html_includes_scripts_or_styles(self, html_content):
        """测试HTML文件是否包含JavaScript脚本或CSS样式"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查脚本和样式
        script_tags = soup.find_all('script')
        style_tags = soup.find_all('style')
        link_css = soup.find_all('link', rel='stylesheet')
        
        has_scripts = len(script_tags) > 0
        has_styles = len(style_tags) > 0 or len(link_css) > 0
        
        assert has_scripts or has_styles, "HTML中未找到JavaScript脚本或CSS样式引用"
    
    def test_html_has_valid_title(self, html_content):
        """测试HTML文件是否有有效的标题"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.find('title')
        
        assert title_tag is not None, "HTML中缺少title标签"
        assert title_tag.string is not None, "title标签为空"
        assert len(title_tag.string.strip()) > 0, "title内容为空"