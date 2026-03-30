import pytest
from pathlib import Path
import re

class TestCanvasRenderingSystem:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        assert index_file.exists(), f"index.html 文件不存在于 {frontend_dir} 目录中"
        assert index_file.is_file(), "index.html 应该是一个文件而不是目录"
    
    def test_index_html_contains_canvas_element(self):
        """测试 index.html 文件是否包含 Canvas 元素和相关渲染系统标签"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查是否包含 canvas 标签
        assert '<canvas' in content.lower(), "HTML 文件应该包含 <canvas> 标签"
        
        # 检查是否包含基本的 HTML 结构
        assert '<html' in content.lower(), "应该包含 <html> 标签"
        assert '<head' in content.lower(), "应该包含 <head> 标签"
        assert '<body' in content.lower(), "应该包含 <body> 标签"
        
        # 检查是否包含 JavaScript 相关内容（Canvas 渲染通常需要 JS）
        js_indicators = ['<script', 'javascript', '.js']
        has_js = any(indicator in content.lower() for indicator in js_indicators)
        assert has_js, "Canvas 渲染系统应该包含 JavaScript 代码或引用"
    
    def test_dev_notes_documentation_exists(self):
        """测试开发文档是否存在并包含项目相关信息"""
        docs_path = Path("docs") / "f1bc12" / "cf550f" / "dev-notes.md"
        
        assert docs_path.exists(), f"开发文档不存在于 {docs_path}"
        assert docs_path.is_file(), "dev-notes.md 应该是一个文件"
        
        content = docs_path.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档不应该为空"
        
        # 检查是否包含与 Canvas 渲染系统相关的关键词
        canvas_keywords = ['canvas', 'render', '渲染', 'frontend', '前端']
        content_lower = content.lower()
        
        has_relevant_content = any(keyword in content_lower for keyword in canvas_keywords)
        assert has_relevant_content, "开发文档应该包含与 Canvas 渲染系统相关的内容"
    
    def test_html_canvas_attributes_and_structure(self):
        """测试 HTML 中 Canvas 元素的属性配置是否合理"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 使用正则表达式查找 canvas 标签
        canvas_pattern = r'<canvas[^>]*>'
        canvas_matches = re.findall(canvas_pattern, content, re.IGNORECASE)
        
        assert len(canvas_matches) > 0, "应该至少包含一个 canvas 元素"
        
        canvas_tag = canvas_matches[0].lower()
        
        # 检查 canvas 是否有基本属性（width, height, id 等）
        recommended_attrs = ['width', 'height', 'id']
        has_attrs = any(attr in canvas_tag for attr in recommended_attrs)
        assert has_attrs, "Canvas 元素应该包含 width、height 或 id 等基本属性"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        # 检查 frontend 目录存在
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend 目录应该存在"
        assert frontend_dir.is_dir(), "frontend 应该是一个目录"
        
        # 检查 docs 目录结构存在
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs 目录应该存在"
        
        nested_docs_dir = docs_dir / "f1bc12" / "cf550f"
        assert nested_docs_dir.exists(), "嵌套的文档目录结构应该存在"
        
        # 检查关键文件都存在
        key_files = [
            frontend_dir / "index.html",
            nested_docs_dir / "dev-notes.md"
        ]
        
        for file_path in key_files:
            assert file_path.exists(), f"关键文件 {file_path} 应该存在"