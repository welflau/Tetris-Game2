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
        """测试HTML文件是否包含消行游戏的关键元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查是否包含游戏区域相关元素
        game_area_selectors = [
            'canvas',  # 游戏画布
            '#game-board',  # 游戏面板ID
            '.game-area',  # 游戏区域类
            '#game-container'  # 游戏容器ID
        ]
        
        has_game_area = any(soup.select(selector) for selector in game_area_selectors)
        assert has_game_area, "HTML中未找到游戏区域相关元素(canvas, #game-board, .game-area, #game-container)"
    
    def test_html_contains_score_system_elements(self, html_content):
        """测试HTML文件是否包含计分系统相关元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查计分相关元素
        score_indicators = []
        
        # 检查是否有分数显示相关的ID或类
        score_selectors = ['#score', '.score', '#current-score', '.current-score']
        for selector in score_selectors:
            if soup.select(selector):
                score_indicators.append(selector)
        
        # 检查是否包含"分数"、"得分"等文本
        text_content = soup.get_text().lower()
        score_keywords = ['分数', '得分', 'score', '积分']
        for keyword in score_keywords:
            if keyword in text_content:
                score_indicators.append(f"文本包含: {keyword}")
        
        assert len(score_indicators) > 0, f"HTML中未找到计分系统相关元素，检查的选择器: {score_selectors}，关键词: {score_keywords}"
    
    def test_html_contains_control_elements(self, html_content):
        """测试HTML文件是否包含游戏控制相关元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查控制按钮
        control_elements = []
        
        # 检查按钮元素
        buttons = soup.find_all('button')
        if buttons:
            control_elements.extend([f"button: {btn.get_text()}" for btn in buttons])
        
        # 检查常见的游戏控制ID和类
        control_selectors = [
            '#start-btn', '#pause-btn', '#restart-btn',
            '.start-button', '.pause-button', '.restart-button',
            '#start', '#pause', '#restart'
        ]
        
        for selector in control_selectors:
            if soup.select(selector):
                control_elements.append(selector)
        
        # 检查是否包含控制相关文本
        text_content = soup.get_text()
        control_keywords = ['开始', '暂停', '重新开始', 'start', 'pause', 'restart', '重置']
        for keyword in control_keywords:
            if keyword in text_content:
                control_elements.append(f"文本包含: {keyword}")
        
        assert len(control_elements) > 0, f"HTML中未找到游戏控制相关元素，找到的元素: {control_elements}"
    
    def test_html_basic_structure(self, html_content):
        """测试HTML文件是否具有基本的HTML结构"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html'), "HTML文件缺少<html>标签"
        assert soup.find('head'), "HTML文件缺少<head>标签"
        assert soup.find('body'), "HTML文件缺少<body>标签"
        
        # 检查是否有标题
        title = soup.find('title')
        assert title is not None, "HTML文件缺少<title>标签"
        
        title_text = title.get_text().strip()
        assert len(title_text) > 0, "HTML文件的title标签为空"