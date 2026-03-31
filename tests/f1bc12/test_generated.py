import pytest
from pathlib import Path
import re

class TestFrontendFiles:
    
    def test_index_html_exists(self):
        """测试前端入口文件index.html是否存在"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), f"前端入口文件不存在: {index_path}"
        assert index_path.is_file(), f"路径不是文件: {index_path}"
    
    def test_index_html_contains_essential_elements(self):
        """测试index.html包含必要的HTML元素和数据持久化相关内容"""
        index_path = Path("frontend/index.html")
        
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head>' in content.lower(), "HTML文件缺少head标签"
        assert '<body>' in content.lower(), "HTML文件缺少body标签"
        assert '<title>' in content.lower(), "HTML文件缺少title标签"
        
        # 检查数据持久化系统相关元素
        content_lower = content.lower()
        persistence_keywords = ['data', 'save', 'load', 'storage', 'database', 'persist']
        has_persistence_content = any(keyword in content_lower for keyword in persistence_keywords)
        assert has_persistence_content, "HTML文件应包含数据持久化相关内容"
    
    def test_dev_notes_file_exists_and_valid(self):
        """测试开发文档dev-notes.md文件存在且包含有效内容"""
        notes_path = Path("docs/f1bc12/46aaab/dev-notes.md")
        
        assert notes_path.exists(), f"开发文档不存在: {notes_path}"
        assert notes_path.is_file(), f"路径不是文件: {notes_path}"
        
        with open(notes_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查文件不为空
        assert len(content.strip()) > 0, "开发文档不能为空"
        
        # 检查是否包含开发相关内容
        dev_keywords = ['开发', 'development', 'todo', 'note', '笔记', '文档', 'api', 'feature']
        content_lower = content.lower()
        has_dev_content = any(keyword in content_lower for keyword in dev_keywords)
        assert has_dev_content, "开发文档应包含开发相关内容"
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构完整性"""
        frontend_dir = Path("frontend")
        docs_dir = Path("docs/f1bc12/46aaab")
        
        assert frontend_dir.exists(), "frontend目录不存在"
        assert frontend_dir.is_dir(), "frontend路径不是目录"
        
        assert docs_dir.exists(), "docs子目录不存在"
        assert docs_dir.is_dir(), "docs路径不是目录"
        
        # 检查目录下至少有指定的文件
        frontend_files = list(frontend_dir.glob("*"))
        assert len(frontend_files) > 0, "frontend目录为空"
        
        docs_files = list(docs_dir.glob("*"))
        assert len(docs_files) > 0, "docs目录为空"
    
    def test_html_syntax_basic_validation(self):
        """测试HTML文件基本语法正确性"""
        index_path = Path("frontend/index.html")
        
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查HTML标签配对
        html_tags = re.findall(r'<(/?)(\w+)[^>]*>', content)
        tag_stack = []
        
        for is_closing, tag_name in html_tags:
            tag_name = tag_name.lower()
            # 跳过自闭合标签
            if tag_name in ['br', 'hr', 'img', 'input', 'meta', 'link']:
                continue
                
            if is_closing == '/':
                assert len(tag_stack) > 0, f"发现未匹配的闭合标签: {tag_name}"
                last_tag = tag_stack.pop()
                assert last_tag == tag_name, f"标签不匹配: 期望 {last_tag}, 实际 {tag_name}"
            else:
                tag_stack.append(tag_name)
        
        # 允许一些标签不闭合（如html, body等在简单页面中）
        remaining_tags = [tag for tag in tag_stack if tag not in ['html', 'head', 'body']]
        assert len(remaining_tags) == 0, f"存在未闭合的标签: {remaining_tags}"