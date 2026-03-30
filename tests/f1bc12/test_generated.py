import pytest
from pathlib import Path
import re

class TestFrontendModule:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        frontend_dir = Path(__file__).parent / "frontend"
        index_file = frontend_dir / "index.html"
        assert index_file.exists(), f"index.html 文件不存在: {index_file}"
        assert index_file.is_file(), f"index.html 不是一个有效文件: {index_file}"
    
    def test_index_html_contains_essential_elements(self):
        """测试 index.html 文件包含游戏引擎必要的HTML元素"""
        frontend_dir = Path(__file__).parent / "frontend"
        index_file = frontend_dir / "index.html"
        
        if not index_file.exists():
            pytest.skip("index.html 文件不存在，跳过内容测试")
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少 <html> 标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少 <head> 标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少 <body> 标签"
        
        # 检查游戏引擎相关元素
        canvas_pattern = r'<canvas[^>]*>'
        script_pattern = r'<script[^>]*>'
        
        assert re.search(canvas_pattern, content, re.IGNORECASE), "缺少游戏渲染用的 <canvas> 元素"
        assert re.search(script_pattern, content, re.IGNORECASE), "缺少 <script> 标签加载游戏引擎"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在并包含有效内容"""
        docs_dir = Path(__file__).parent / "docs" / "f1bc12" / "a3798c"
        dev_notes_file = docs_dir / "dev-notes.md"
        
        assert dev_notes_file.exists(), f"开发文档不存在: {dev_notes_file}"
        assert dev_notes_file.is_file(), f"dev-notes.md 不是一个有效文件: {dev_notes_file}"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含游戏引擎开发相关关键词
        engine_keywords = ['游戏引擎', 'game engine', '核心架构', 'core', 'frontend', '前端']
        content_lower = content.lower()
        
        has_relevant_content = any(keyword.lower() in content_lower for keyword in engine_keywords)
        assert has_relevant_content, "开发文档缺少游戏引擎相关内容描述"
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构的完整性"""
        frontend_dir = Path(__file__).parent / "frontend"
        docs_dir = Path(__file__).parent / "docs"
        
        assert frontend_dir.exists(), f"frontend 目录不存在: {frontend_dir}"
        assert docs_dir.exists(), f"docs 目录不存在: {docs_dir}"
        
        # 检查关键文件
        required_files = [
            frontend_dir / "index.html",
            docs_dir / "f1bc12" / "a3798c" / "dev-notes.md"
        ]
        
        for file_path in required_files:
            assert file_path.exists(), f"必需文件缺失: {file_path}"
    
    def test_html_file_encoding_and_syntax(self):
        """测试HTML文件编码正确且语法基本有效"""
        frontend_dir = Path(__file__).parent / "frontend"
        index_file = frontend_dir / "index.html"
        
        if not index_file.exists():
            pytest.skip("index.html 文件不存在，跳过语法测试")
        
        # 测试文件可以用UTF-8编码正确读取
        try:
            content = index_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            pytest.fail("HTML文件编码不是UTF-8或包含无效字符")
        
        # 基本语法检查：标签配对
        open_tags = len(re.findall(r'<html[^>]*>', content, re.IGNORECASE))
        close_tags = len(re.findall(r'</html>', content, re.IGNORECASE))
        
        if open_tags > 0:
            assert open_tags == close_tags, "HTML标签未正确闭合"