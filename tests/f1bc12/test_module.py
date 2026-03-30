import pytest
from pathlib import Path
import re

class TestFrontendModule:
    """前端模块测试类"""
    
    def test_index_html_file_exists(self):
        """测试index.html文件是否存在"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        assert index_file.exists(), f"index.html文件不存在于{frontend_dir}目录中"
        assert index_file.is_file(), "index.html应该是一个文件而不是目录"
    
    def test_index_html_contains_essential_elements(self):
        """测试index.html文件是否包含基本的HTML结构元素"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        # 确保文件存在
        assert index_file.exists(), "index.html文件不存在"
        
        # 读取文件内容
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<!DOCTYPE\s+html>', content, re.IGNORECASE), "缺少DOCTYPE声明"
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少html标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少head标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少body标签"
        assert re.search(r'<title[^>]*>.*</title>', content, re.IGNORECASE), "缺少title标签"
    
    def test_index_html_has_valid_structure(self):
        """测试index.html文件是否具有有效的HTML文档结构"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        assert index_file.exists(), "index.html文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查标签是否正确闭合（基本检查）
        open_tags = len(re.findall(r'<html[^>]*>', content, re.IGNORECASE))
        close_tags = len(re.findall(r'</html>', content, re.IGNORECASE))
        assert open_tags == close_tags, "html标签未正确闭合"
        
        open_head = len(re.findall(r'<head[^>]*>', content, re.IGNORECASE))
        close_head = len(re.findall(r'</head>', content, re.IGNORECASE))
        assert open_head == close_head, "head标签未正确闭合"
        
        open_body = len(re.findall(r'<body[^>]*>', content, re.IGNORECASE))
        close_body = len(re.findall(r'</body>', content, re.IGNORECASE))
        assert open_body == close_body, "body标签未正确闭合"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        docs_path = Path("docs/f1bc12/c3f0c7/dev-notes.md")
        assert docs_path.exists(), f"开发文档文件不存在于{docs_path}路径"
        assert docs_path.is_file(), "dev-notes.md应该是一个文件而不是目录"
    
    def test_dev_notes_has_content(self):
        """测试开发文档文件是否包含有效内容"""
        docs_path = Path("docs/f1bc12/c3f0c7/dev-notes.md")
        
        assert docs_path.exists(), "开发文档文件不存在"
        
        content = docs_path.read_text(encoding='utf-8')
        
        # 检查文件不为空
        assert len(content.strip()) > 0, "开发文档文件内容为空"
        
        # 检查是否包含markdown格式的标题
        has_headers = bool(re.search(r'^#+\s+.+', content, re.MULTILINE))
        assert has_headers, "开发文档应该包含markdown格式的标题"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性"""
        # 检查frontend目录存在
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend目录不存在"
        assert frontend_dir.is_dir(), "frontend应该是一个目录"
        
        # 检查docs目录结构存在
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs目录不存在"
        
        nested_dir = Path("docs/f1bc12/c3f0c7")
        assert nested_dir.exists(), "docs子目录结构不完整"
        assert nested_dir.is_dir(), "docs/f1bc12/c3f0c7应该是一个目录"