import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestFrontendPerformanceOptimization:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_performance_elements(self):
        """测试 index.html 是否包含性能优化相关的关键元素"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否包含基本的HTML结构
        assert soup.find('html'), "HTML文件缺少html标签"
        assert soup.find('head'), "HTML文件缺少head标签"
        assert soup.find('body'), "HTML文件缺少body标签"
        
        # 检查性能优化相关元素
        meta_viewport = soup.find('meta', attrs={'name': 'viewport'})
        assert meta_viewport is not None, "缺少viewport meta标签，影响移动端性能"
        
        # 检查是否有CSS或JS引用（性能优化项目应该有样式和脚本）
        has_css = soup.find('link', rel='stylesheet') or soup.find('style')
        has_js = soup.find('script')
        assert has_css or has_js, "HTML文件应包含CSS样式或JavaScript脚本"
    
    def test_index_html_contains_animation_elements(self):
        """测试 index.html 是否包含动画效果相关的元素或属性"""
        index_file = Path("frontend/index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read().lower()
        
        # 检查动画相关的关键词
        animation_keywords = [
            'animation', 'transition', 'transform', 'keyframes',
            'animate', 'fade', 'slide', 'rotate', 'scale'
        ]
        
        has_animation = any(keyword in content for keyword in animation_keywords)
        assert has_animation, "HTML文件应包含动画效果相关的CSS类名、属性或JavaScript代码"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读"""
        dev_notes_file = Path("docs/f1bc12/7fc47c/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档 dev-notes.md 文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md 不是一个有效的文件"
        
        # 检查文件是否可读且不为空
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        assert len(content) > 0, "开发文档文件不应为空"
        assert len(content) > 50, "开发文档内容过少，应包含更详细的说明"
    
    def test_dev_notes_contains_project_info(self):
        """测试开发文档是否包含项目相关信息"""
        dev_notes_file = Path("docs/f1bc12/7fc47c/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        
        with open(dev_notes_file, 'r', encoding='utf-8') as f:
            content = f.read().lower()
        
        # 检查是否包含性能优化或动画相关的关键词
        project_keywords = [
            '性能', 'performance', '优化', 'optimization',
            '动画', 'animation', '效果', 'effect',
            'frontend', '前端'
        ]
        
        keyword_found = any(keyword in content for keyword in project_keywords)
        assert keyword_found, "开发文档应包含项目相关的关键词说明"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        # 检查frontend目录存在
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend 目录不存在"
        assert frontend_dir.is_dir(), "frontend 应该是一个目录"
        
        # 检查docs目录结构存在
        docs_dir = Path("docs/f1bc12/7fc47c")
        assert docs_dir.exists(), "文档目录结构不完整"
        assert docs_dir.is_dir(), "docs/f1bc12/7fc47c 应该是一个目录"
        
        # 检查关键文件都存在
        key_files = [
            Path("frontend/index.html"),
            Path("docs/f1bc12/7fc47c/dev-notes.md")
        ]
        
        for file_path in key_files:
            assert file_path.exists(), f"关键文件 {file_path} 不存在"