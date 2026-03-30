import pytest
from pathlib import Path
import re

class TestFrontendFiles:
    """测试前端文件的存在性和内容"""
    
    def test_index_html_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_essential_elements(self):
        """测试 index.html 文件包含必要的HTML元素"""
        index_file = Path("frontend/index.html")
        
        if not index_file.exists():
            pytest.skip("index.html 文件不存在，跳过内容测试")
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert re.search(r'<html[^>]*>', content, re.IGNORECASE), "缺少 <html> 标签"
        assert re.search(r'<head[^>]*>', content, re.IGNORECASE), "缺少 <head> 标签"
        assert re.search(r'<body[^>]*>', content, re.IGNORECASE), "缺少 <body> 标签"
        
        # 检查投影方块相关的关键词
        content_lower = content.lower()
        projection_keywords = ['投影', 'projection', '方块', 'block', 'cube', '配置', 'config']
        found_keywords = [keyword for keyword in projection_keywords if keyword in content_lower]
        assert len(found_keywords) > 0, f"HTML内容中未找到投影方块相关关键词: {projection_keywords}"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        dev_notes_file = Path("docs/35cf91/5a8a3f/dev-notes.md")
        
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
        
        # 测试文件是否可读且不为空
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档文件内容为空"
        
        # 检查是否包含Markdown格式的内容
        markdown_indicators = ['#', '##', '###', '-', '*', '```', '**', '__']
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "开发文档似乎不包含Markdown格式内容"

class TestProjectStructure:
    """测试项目结构的完整性"""
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构是否合理"""
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend 目录不存在"
        assert frontend_dir.is_dir(), "frontend 不是一个目录"
        
        # 检查前端目录下是否有基本文件
        files_in_frontend = list(frontend_dir.iterdir())
        assert len(files_in_frontend) > 0, "frontend 目录为空"
        
        # 检查是否有HTML文件
        html_files = [f for f in files_in_frontend if f.suffix.lower() == '.html']
        assert len(html_files) > 0, "frontend 目录中没有HTML文件"
    
    def test_docs_directory_structure(self):
        """测试文档目录结构是否存在"""
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs 目录不存在"
        assert docs_dir.is_dir(), "docs 不是一个目录"
        
        # 检查特定的子目录路径
        specific_path = Path("docs/35cf91/5a8a3f")
        assert specific_path.exists(), "指定的文档子目录路径不存在"
        assert specific_path.is_dir(), "指定的路径不是目录"
    
    def test_project_configuration_files(self):
        """测试项目配置相关文件的存在性"""
        project_root = Path(".")
        
        # 常见的项目配置文件
        possible_config_files = [
            "package.json",
            "requirements.txt", 
            "pyproject.toml",
            "setup.py",
            "README.md",
            "README.rst",
            ".gitignore"
        ]
        
        existing_config_files = []
        for config_file in possible_config_files:
            file_path = project_root / config_file
            if file_path.exists():
                existing_config_files.append(config_file)
        
        # 至少应该有一个配置文件存在
        assert len(existing_config_files) > 0, f"项目根目录下未找到任何常见配置文件: {possible_config_files}"