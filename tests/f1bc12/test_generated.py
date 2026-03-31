import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestUserControlSystemFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_essential_elements(self):
        """测试 index.html 文件包含用户控制系统的基本HTML元素"""
        index_file = Path("frontend/index.html")
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html') is not None, "缺少 html 标签"
        assert soup.find('head') is not None, "缺少 head 标签"
        assert soup.find('body') is not None, "缺少 body 标签"
        
        # 检查用户控制系统相关元素
        title = soup.find('title')
        assert title is not None, "缺少 title 标签"
        
        # 检查是否包含用户控制相关的关键词
        page_text = content.lower()
        user_control_keywords = ['user', 'login', 'control', 'system', '用户', '登录', '控制', '系统']
        has_keywords = any(keyword in page_text for keyword in user_control_keywords)
        assert has_keywords, "页面内容缺少用户控制系统相关关键词"
    
    def test_index_html_has_form_elements(self):
        """测试 index.html 包含用户交互表单元素"""
        index_file = Path("frontend/index.html")
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否有表单或输入元素（用户控制系统通常需要）
        forms = soup.find_all('form')
        inputs = soup.find_all('input')
        buttons = soup.find_all('button')
        
        # 至少应该有输入框或按钮等交互元素
        interactive_elements = len(forms) + len(inputs) + len(buttons)
        assert interactive_elements > 0, "页面缺少用户交互元素（表单、输入框或按钮）"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        dev_notes_file = Path("docs/f1bc12/051d21/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
        
        # 检查文件是否可读且不为空
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            assert len(content) > 0, "开发文档文件为空"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性"""
        # 检查前端目录存在
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend 目录不存在"
        assert frontend_dir.is_dir(), "frontend 不是一个目录"
        
        # 检查文档目录结构存在
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs 目录不存在"
        
        nested_docs_dir = Path("docs/f1bc12/051d21")
        assert nested_docs_dir.exists(), "嵌套文档目录结构不完整"