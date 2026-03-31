import pytest
from pathlib import Path
import re

class TestFrontendModule:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        assert index_file.exists(), f"index.html 文件不存在于 {frontend_dir} 目录中"
        assert index_file.is_file(), "index.html 应该是一个文件而不是目录"
    
    def test_index_html_contains_game_elements(self):
        """测试 index.html 文件包含游戏相关的关键元素"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        if not index_file.exists():
            pytest.skip("index.html 文件不存在，跳过内容测试")
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert "<html" in content.lower(), "HTML文件应包含html标签"
        assert "<head>" in content.lower() or "<head " in content.lower(), "HTML文件应包含head标签"
        assert "<body>" in content.lower() or "<body " in content.lower(), "HTML文件应包含body标签"
        
        # 检查游戏相关元素
        game_keywords = ["game", "play", "start", "score", "level", "canvas", "游戏", "开始", "分数"]
        has_game_element = any(keyword in content.lower() for keyword in game_keywords)
        assert has_game_element, f"HTML文件应包含游戏相关关键词: {game_keywords}"
    
    def test_index_html_has_valid_structure(self):
        """测试 index.html 文件具有有效的HTML结构"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        if not index_file.exists():
            pytest.skip("index.html 文件不存在，跳过结构测试")
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查DOCTYPE声明
        has_doctype = content.strip().lower().startswith('<!doctype') or '<html' in content.lower()
        assert has_doctype, "HTML文件应包含DOCTYPE声明或html标签"
        
        # 检查标题标签
        has_title = "<title>" in content.lower() and "</title>" in content.lower()
        assert has_title, "HTML文件应包含title标签"
        
        # 检查是否有JavaScript或CSS引用（游戏逻辑需要）
        has_script_or_style = ("<script" in content.lower() or 
                              "<style" in content.lower() or 
                              'rel="stylesheet"' in content.lower())
        assert has_script_or_style, "游戏HTML文件应包含JavaScript或CSS引用"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        docs_dir = Path("docs/f1bc12/e2e094")
        dev_notes_file = docs_dir / "dev-notes.md"
        assert dev_notes_file.exists(), f"dev-notes.md 文件不存在于 {docs_dir} 目录中"
        assert dev_notes_file.is_file(), "dev-notes.md 应该是一个文件而不是目录"
    
    def test_dev_notes_contains_documentation(self):
        """测试开发文档包含有效的文档内容"""
        docs_dir = Path("docs/f1bc12/e2e094")
        dev_notes_file = docs_dir / "dev-notes.md"
        
        if not dev_notes_file.exists():
            pytest.skip("dev-notes.md 文件不存在，跳过内容测试")
        
        content = dev_notes_file.read_text(encoding='utf-8')
        
        # 检查文档不为空
        assert len(content.strip()) > 0, "开发文档不应为空"
        
        # 检查是否包含Markdown格式内容
        markdown_indicators = ["#", "##", "###", "*", "-", "`", "```", "**"]
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "开发文档应包含Markdown格式标记"
        
        # 检查是否包含开发相关关键词
        dev_keywords = ["开发", "功能", "实现", "设计", "架构", "api", "接口", "模块", "组件"]
        has_dev_content = any(keyword in content.lower() for keyword in dev_keywords)
        assert has_dev_content, f"开发文档应包含开发相关内容: {dev_keywords}"