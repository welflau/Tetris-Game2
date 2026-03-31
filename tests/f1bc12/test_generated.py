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
    
    def test_html_contains_essential_elements(self, html_content):
        """测试HTML文件是否包含基本的HTML结构元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html') is not None, "HTML文件缺少<html>标签"
        assert soup.find('head') is not None, "HTML文件缺少<head>标签"
        assert soup.find('body') is not None, "HTML文件缺少<body>标签"
        assert soup.find('title') is not None, "HTML文件缺少<title>标签"
    
    def test_html_contains_data_persistence_ui_elements(self, html_content):
        """测试HTML文件是否包含数据持久化系统相关的UI元素"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查是否包含表单元素（用于数据输入）
        forms = soup.find_all('form')
        inputs = soup.find_all('input')
        buttons = soup.find_all('button')
        
        # 至少应该有一些交互元素
        interactive_elements = len(forms) + len(inputs) + len(buttons)
        assert interactive_elements > 0, "HTML文件缺少数据输入相关的交互元素（表单、输入框或按钮）"
        
        # 检查是否有用于显示数据的容器元素
        containers = soup.find_all(['div', 'section', 'article', 'table'])
        assert len(containers) > 0, "HTML文件缺少用于显示数据的容器元素"
    
    def test_html_has_valid_structure(self, html_content):
        """测试HTML文件是否具有有效的文档结构"""
        assert html_content is not None, "无法读取HTML文件内容"
        
        # 检查是否包含DOCTYPE声明
        assert '<!DOCTYPE' in html_content.upper() or '<html' in html_content, "HTML文件缺少DOCTYPE声明或HTML标签"
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 检查title标签是否有内容
        title = soup.find('title')
        if title:
            assert title.get_text().strip() != "", "title标签内容为空"
        
        # 检查是否有meta标签（字符编码等）
        meta_tags = soup.find_all('meta')
        charset_found = any('charset' in str(meta) for meta in meta_tags)
        assert charset_found or 'charset' in html_content.lower(), "HTML文件缺少字符编码声明"