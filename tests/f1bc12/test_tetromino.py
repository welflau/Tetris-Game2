import pytest
from pathlib import Path
import re

class TestTetrominoFrontend:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_tetromino_elements(self):
        """测试 index.html 文件包含俄罗斯方块游戏的关键元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "缺少 HTML 标签"
        assert '<head>' in content.lower(), "缺少 head 标签"
        assert '<body>' in content.lower(), "缺少 body 标签"
        
        # 检查游戏相关元素
        tetromino_keywords = ['tetromino', 'tetris', 'block', 'game', 'canvas', 'grid']
        has_game_element = any(keyword in content.lower() for keyword in tetromino_keywords)
        assert has_game_element, "HTML内容中缺少俄罗斯方块游戏相关的关键元素"
    
    def test_index_html_has_valid_structure(self):
        """测试 index.html 文件具有有效的HTML结构和游戏容器"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        content = index_file.read_text(encoding='utf-8')
        
        # 检查DOCTYPE声明
        assert '<!doctype html>' in content.lower() or '<!DOCTYPE html>' in content, "缺少 DOCTYPE 声明"
        
        # 检查是否有游戏容器元素（div、canvas等）
        container_patterns = [
            r'<div[^>]*id[^>]*>',
            r'<canvas[^>]*>',
            r'<div[^>]*class[^>]*game[^>]*>',
            r'<div[^>]*class[^>]*tetris[^>]*>'
        ]
        
        has_container = any(re.search(pattern, content, re.IGNORECASE) for pattern in container_patterns)
        assert has_container, "HTML中缺少游戏容器元素（如带id的div或canvas标签）"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        dev_notes_file = Path("docs/f1bc12/353111/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
        
        # 检查文件是否可读且不为空
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档文件为空"
    
    def test_dev_notes_contains_project_info(self):
        """测试开发文档包含项目相关信息"""
        dev_notes_file = Path("docs/f1bc12/353111/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        
        # 检查是否包含项目相关的关键词
        project_keywords = ['tetromino', 'tetris', 'block', 'game', 'frontend', 'development', '开发', '方块']
        has_project_info = any(keyword.lower() in content.lower() for keyword in project_keywords)
        assert has_project_info, "开发文档中缺少项目相关信息"
        
        # 检查是否有markdown格式的标题
        has_markdown_headers = '#' in content
        assert has_markdown_headers, "开发文档缺少markdown格式的标题结构"