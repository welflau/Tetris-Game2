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
    
    def test_html_contains_canvas_element(self, html_content):
        """测试HTML文件是否包含用于渲染Tetromino游戏的canvas元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        soup = BeautifulSoup(html_content, 'html.parser')
        canvas_elements = soup.find_all('canvas')
        assert len(canvas_elements) > 0, "HTML文件中缺少canvas元素，无法渲染游戏画面"
        
        # 检查canvas是否有合适的属性
        main_canvas = canvas_elements[0]
        assert main_canvas.get('id') or main_canvas.get('class'), "canvas元素缺少id或class属性"
    
    def test_html_contains_game_controls(self, html_content):
        """测试HTML文件是否包含游戏控制相关的元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查是否有按钮或输入控制元素
        control_elements = soup.find_all(['button', 'input', 'div'])
        control_keywords = ['start', 'pause', 'reset', 'control', 'game', 'score']
        
        has_control_elements = False
        for element in control_elements:
            element_text = str(element).lower()
            if any(keyword in element_text for keyword in control_keywords):
                has_control_elements = True
                break
        
        assert has_control_elements, "HTML文件中缺少游戏控制相关的元素"
    
    def test_html_includes_javascript(self, html_content):
        """测试HTML文件是否包含JavaScript代码或引用，用于实现Tetromino游戏逻辑"""
        assert html_content is not None, "无法读取HTML文件内容"
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查是否有script标签
        script_elements = soup.find_all('script')
        has_js = len(script_elements) > 0
        
        # 检查是否有外部JS文件引用或内联JS代码
        if has_js:
            for script in script_elements:
                if script.get('src') or script.string:
                    has_js = True
                    break
        
        assert has_js, "HTML文件中缺少JavaScript代码，无法实现Tetromino游戏功能"
    
    def test_html_has_proper_structure(self, html_content):
        """测试HTML文件是否具有正确的基本结构"""
        assert html_content is not None, "无法读取HTML文件内容"
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html'), "HTML文件缺少html标签"
        assert soup.find('head'), "HTML文件缺少head标签"
        assert soup.find('body'), "HTML文件缺少body标签"
        
        # 检查title标签
        title = soup.find('title')
        assert title is not None, "HTML文件缺少title标签"
        title_text = title.get_text().lower()
        assert 'tetromino' in title_text or 'tetris' in title_text or '俄罗斯方块' in title_text, "页面标题应该包含游戏相关关键词"