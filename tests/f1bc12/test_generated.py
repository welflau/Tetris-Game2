import pytest
from pathlib import Path
import re

class TestLeaderboardFrontend:
    
    def test_index_html_file_exists(self):
        """测试排行榜首页HTML文件是否存在"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        assert index_file.exists(), f"排行榜首页文件 {index_file} 不存在"
        assert index_file.is_file(), f"{index_file} 不是一个有效的文件"
    
    def test_index_html_contains_leaderboard_elements(self):
        """测试首页HTML包含排行榜必要的页面元素"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read().lower()
        
        # 检查基本HTML结构
        assert '<html' in content, "HTML文件缺少html标签"
        assert '<head>' in content, "HTML文件缺少head标签"
        assert '<body>' in content, "HTML文件缺少body标签"
        
        # 检查排行榜相关元素
        leaderboard_keywords = ['排行榜', 'leaderboard', 'ranking', '排名']
        has_leaderboard_keyword = any(keyword in content for keyword in leaderboard_keywords)
        assert has_leaderboard_keyword, "HTML文件缺少排行榜相关关键词"
    
    def test_index_html_has_valid_structure(self):
        """测试首页HTML具有有效的表格或列表结构用于显示排行数据"""
        frontend_dir = Path("frontend")
        index_file = frontend_dir / "index.html"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read().lower()
        
        # 检查是否包含表格或列表结构
        has_table = '<table' in content and '</table>' in content
        has_list = ('<ul' in content and '</ul>' in content) or ('<ol' in content and '</ol>' in content)
        has_div_structure = '<div' in content and 'class' in content
        
        assert has_table or has_list or has_div_structure, "HTML文件缺少用于显示排行数据的结构元素（表格、列表或div容器）"
    
    def test_dev_notes_file_exists_and_readable(self):
        """测试开发文档文件是否存在且可读取"""
        docs_path = Path("docs/f1bc12/4734db/dev-notes.md")
        assert docs_path.exists(), f"开发文档文件 {docs_path} 不存在"
        assert docs_path.is_file(), f"{docs_path} 不是一个有效的文件"
        
        # 测试文件是否可读
        try:
            with open(docs_path, 'r', encoding='utf-8') as f:
                content = f.read()
            assert len(content) > 0, "开发文档文件为空"
        except Exception as e:
            pytest.fail(f"无法读取开发文档文件: {e}")
    
    def test_frontend_directory_structure(self):
        """测试前端目录结构是否完整"""
        frontend_dir = Path("frontend")
        assert frontend_dir.exists(), "frontend目录不存在"
        assert frontend_dir.is_dir(), "frontend不是一个目录"
        
        # 检查前端项目常见文件
        common_files = ["index.html"]
        for file_name in common_files:
            file_path = frontend_dir / file_name
            assert file_path.exists(), f"前端项目缺少必要文件: {file_name}"