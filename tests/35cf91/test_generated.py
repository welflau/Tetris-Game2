import pytest
from pathlib import Path
import re

class TestProjectionBlockTransparencyFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), "index.html 文件不存在"
        assert index_path.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_transparency_elements(self):
        """测试 index.html 是否包含透明度调整相关的关键元素"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), "index.html 文件不存在"
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查是否包含透明度相关的关键词
        transparency_keywords = ['透明度', 'transparency', 'opacity', 'alpha']
        has_transparency_keyword = any(keyword in content.lower() for keyword in transparency_keywords)
        assert has_transparency_keyword, "HTML内容中未找到透明度相关关键词"
        
        # 检查是否包含滑块或输入控件
        control_patterns = [
            r'<input[^>]*type=["\']range["\']',
            r'<input[^>]*type=["\']number["\']',
            r'<slider',
            r'opacity',
            r'透明度'
        ]
        has_control = any(re.search(pattern, content, re.IGNORECASE) for pattern in control_patterns)
        assert has_control, "HTML内容中未找到透明度调整控件"
    
    def test_dev_notes_file_exists_and_contains_project_info(self):
        """测试开发文档是否存在并包含项目相关信息"""
        dev_notes_path = Path("docs/35cf91/5cd167/dev-notes.md")
        assert dev_notes_path.exists(), "开发文档 dev-notes.md 不存在"
        assert dev_notes_path.is_file(), "dev-notes.md 不是一个有效的文件"
        
        content = dev_notes_path.read_text(encoding='utf-8')
        
        # 检查是否包含项目相关信息
        project_keywords = ['投影', '方块', '透明度', 'projection', 'block', 'transparency', 'opacity']
        has_project_keyword = any(keyword in content for keyword in project_keywords)
        assert has_project_keyword, "开发文档中未找到项目相关关键词"
        
        # 检查文档是否有实际内容（不是空文件）
        assert len(content.strip()) > 0, "开发文档内容为空"
    
    def test_html_structure_validity(self):
        """测试 HTML 文件的基本结构是否有效"""
        index_path = Path("frontend/index.html")
        assert index_path.exists(), "index.html 文件不存在"
        
        content = index_path.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head' in content.lower(), "HTML文件缺少head标签"
        assert '<body' in content.lower(), "HTML文件缺少body标签"
        
        # 检查是否有标题
        has_title = '<title' in content.lower() or '<h1' in content.lower() or '<h2' in content.lower()
        assert has_title, "HTML文件缺少标题元素"
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构是否正确"""
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend 目录不存在"
        assert frontend_dir.is_dir(), "frontend 不是一个目录"
        
        # 检查必要文件
        required_files = ["index.html"]
        for file_name in required_files:
            file_path = frontend_dir / file_name
            assert file_path.exists(), f"前端目录中缺少必要文件: {file_name}"