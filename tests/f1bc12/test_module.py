import pytest
from pathlib import Path
import re

class TestFrontendPerformanceAndAnimation:
    
    def test_index_html_file_exists(self):
        """测试index.html文件是否存在"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        assert index_file.exists(), f"index.html文件不存在于{frontend_dir}目录中"
        assert index_file.is_file(), "index.html应该是一个文件而不是目录"
    
    def test_index_html_contains_performance_elements(self):
        """测试index.html是否包含性能优化相关的关键元素"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查HTML基本结构
        assert '<html' in content.lower(), "HTML文件应包含html标签"
        assert '<head>' in content.lower(), "HTML文件应包含head标签"
        assert '<body>' in content.lower(), "HTML文件应包含body标签"
        
        # 检查性能优化相关元素
        performance_indicators = [
            'viewport',  # 响应式设计
            'preload',   # 资源预加载
            'defer',     # 脚本延迟加载
            'async',     # 异步加载
            'loading="lazy"',  # 图片懒加载
        ]
        
        found_indicators = [indicator for indicator in performance_indicators if indicator in content.lower()]
        assert len(found_indicators) >= 1, f"HTML文件应包含至少一个性能优化元素，找到的元素: {found_indicators}"
    
    def test_index_html_contains_animation_elements(self):
        """测试index.html是否包含动画效果相关的元素"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查动画相关元素
        animation_indicators = [
            'animation',
            'transition',
            'transform',
            'keyframes',
            '@keyframes',
            'animate',
            'css',
            'style',
        ]
        
        found_animations = [indicator for indicator in animation_indicators if indicator in content.lower()]
        assert len(found_animations) >= 1, f"HTML文件应包含动画相关元素，找到的元素: {found_animations}"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        docs_path = Path("docs/f1bc12/7fc47c/dev-notes.md")
        assert docs_path.exists(), f"开发文档文件不存在: {docs_path}"
        assert docs_path.is_file(), "dev-notes.md应该是一个文件"
        
        # 测试文件是否可读
        with open(docs_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert len(content) > 0, "开发文档文件不应为空"
        assert isinstance(content, str), "文档内容应为字符串类型"
    
    def test_dev_notes_contains_project_info(self):
        """测试开发文档是否包含项目相关信息"""
        docs_path = Path("docs/f1bc12/7fc47c/dev-notes.md")
        
        with open(docs_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查文档是否包含项目相关关键词
        project_keywords = [
            '性能',
            '优化',
            '动画',
            'performance',
            'animation',
            'frontend',
            '前端',
        ]
        
        found_keywords = [keyword for keyword in project_keywords if keyword.lower() in content.lower()]
        assert len(found_keywords) >= 2, f"开发文档应包含至少2个项目相关关键词，找到: {found_keywords}"
    
    def test_html_file_structure_validity(self):
        """测试HTML文件结构的有效性"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查HTML标签配对
        html_tags = ['html', 'head', 'body', 'title']
        for tag in html_tags:
            open_tag_pattern = f'<{tag}[^>]*>'
            close_tag_pattern = f'</{tag}>'
            
            open_matches = len(re.findall(open_tag_pattern, content, re.IGNORECASE))
            close_matches = len(re.findall(close_tag_pattern, content, re.IGNORECASE))
            
            if open_matches > 0:  # 如果存在开标签，则应该有对应的闭标签
                assert open_matches == close_matches, f"标签{tag}的开闭标签数量不匹配: 开标签{open_matches}个，闭标签{close_matches}个"