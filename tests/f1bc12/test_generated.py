import pytest
from pathlib import Path
import re

class TestDesignModule:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("design/index.html")
        assert index_file.exists(), f"index.html 文件不存在: {index_file}"
        assert index_file.is_file(), f"{index_file} 不是一个有效的文件"
    
    def test_index_html_contains_essential_elements(self):
        """测试 index.html 文件包含必要的 HTML 元素"""
        index_file = Path("design/index.html")
        
        if not index_file.exists():
            pytest.skip("index.html 文件不存在，跳过内容测试")
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本 HTML 结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少 <html> 标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少 <head> 标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少 <body> 标签"
        
        # 检查用户界面相关元素
        ui_elements = ['<div', '<button', '<input', '<form', '<nav']
        has_ui_element = any(element in content.lower() for element in ui_elements)
        assert has_ui_element, "HTML 文件应包含至少一个用户界面元素 (div, button, input, form, nav)"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在并包含有效内容"""
        dev_notes_file = Path("design/docs/f1bc12/0556e3/dev-notes.md")
        
        assert dev_notes_file.exists(), f"开发文档不存在: {dev_notes_file}"
        assert dev_notes_file.is_file(), f"{dev_notes_file} 不是一个有效的文件"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档不能为空"
        
        # 检查是否包含开发相关的关键词
        dev_keywords = ['设计', '开发', '实现', '功能', '界面', 'UI', 'UX', '需求']
        has_dev_content = any(keyword in content for keyword in dev_keywords)
        assert has_dev_content, "开发文档应包含设计或开发相关的内容"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        design_dir = Path("design")
        assert design_dir.exists(), "design 目录不存在"
        assert design_dir.is_dir(), "design 应该是一个目录"
        
        docs_dir = Path("design/docs")
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs 应该是一个目录"
        
        # 检查是否有其他常见的前端文件
        common_files = ["style.css", "script.js", "main.css", "app.js"]
        existing_files = [f for f in common_files if (design_dir / f).exists()]
        
        # 至少应该有 index.html 存在
        essential_files = list(design_dir.glob("*.html"))
        assert len(essential_files) > 0, "design 目录应至少包含一个 HTML 文件"
    
    def test_html_file_encoding_and_syntax(self):
        """测试 HTML 文件的编码和基本语法正确性"""
        index_file = Path("design/index.html")
        
        if not index_file.exists():
            pytest.skip("index.html 文件不存在，跳过语法测试")
        
        # 测试文件可以用 UTF-8 编码读取
        try:
            content = index_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            pytest.fail("HTML 文件编码不是 UTF-8 或包含无效字符")
        
        # 检查基本的 HTML 标签配对
        open_tags = len(re.findall(r'<html[^>]*>', content, re.IGNORECASE))
        close_tags = len(re.findall(r'</html>', content, re.IGNORECASE))
        
        if open_tags > 0:
            assert open_tags == close_tags, "HTML 标签未正确闭合"