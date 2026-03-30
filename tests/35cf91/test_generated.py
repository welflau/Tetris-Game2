import pytest
import json
from pathlib import Path
from bs4 import BeautifulSoup

class TestCrossBrowserCompatibility:
    
    def test_index_html_file_exists(self):
        """测试 index.html 文件是否存在"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        assert index_file.is_file(), "index.html 不是一个有效的文件"
    
    def test_index_html_contains_essential_elements(self):
        """测试 index.html 文件包含跨浏览器测试必需的关键元素"""
        index_file = Path("index.html")
        assert index_file.exists(), "index.html 文件不存在"
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 检查基本HTML结构
        assert soup.find('html'), "HTML文档缺少html标签"
        assert soup.find('head'), "HTML文档缺少head标签"
        assert soup.find('body'), "HTML文档缺少body标签"
        
        # 检查跨浏览器兼容性相关元素
        assert soup.find('meta', {'charset': True}), "缺少字符编码声明"
        
        # 检查是否包含viewport元数据（移动端兼容性）
        viewport_meta = soup.find('meta', {'name': 'viewport'})
        assert viewport_meta is not None, "缺少viewport元数据标签"
        
        # 检查是否有标题
        assert soup.find('title'), "HTML文档缺少title标签"
    
    def test_config_file_structure_and_browser_settings(self):
        """测试配置文件结构和浏览器设置的有效性"""
        config_file = Path("test-config.json")
        assert config_file.exists(), "test-config.json 配置文件不存在"
        
        with open(config_file, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        
        # 检查配置文件基本结构
        assert isinstance(config_data, dict), "配置文件应该是一个JSON对象"
        
        # 检查浏览器配置
        if 'browsers' in config_data:
            browsers = config_data['browsers']
            assert isinstance(browsers, list), "browsers配置应该是一个数组"
            
            # 验证常见浏览器配置
            browser_names = [browser.get('name', '').lower() for browser in browsers if isinstance(browser, dict)]
            expected_browsers = ['chrome', 'firefox', 'safari', 'edge']
            
            # 至少应该包含两种主流浏览器
            common_browsers_count = sum(1 for browser in expected_browsers if browser in str(browser_names).lower())
            assert common_browsers_count >= 2, f"配置文件应包含至少2种主流浏览器，当前只有: {browser_names}"
        
        # 检查测试环境配置
        if 'testEnvironments' in config_data:
            test_envs = config_data['testEnvironments']
            assert isinstance(test_envs, list), "testEnvironments应该是一个数组"
    
    def test_documentation_file_exists_and_content(self):
        """测试开发文档是否存在并包含有效内容"""
        doc_file = Path("docs/35cf91/64891c/dev-notes.md")
        assert doc_file.exists(), "开发文档 dev-notes.md 不存在"
        assert doc_file.is_file(), "dev-notes.md 不是一个有效的文件"
        
        with open(doc_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查文档内容不为空
        assert len(content.strip()) > 0, "开发文档内容为空"
        
        # 检查是否包含跨浏览器测试相关关键词
        content_lower = content.lower()
        compatibility_keywords = ['browser', 'compatibility', 'test', '浏览器', '兼容', '测试']
        
        keyword_found = any(keyword in content_lower for keyword in compatibility_keywords)
        assert keyword_found, f"开发文档应包含跨浏览器兼容性测试相关内容，期望关键词: {compatibility_keywords}"
    
    def test_project_structure_completeness(self):
        """测试项目结构的完整性"""
        required_files = [
            Path("index.html"),
            Path("test-config.json"),
            Path("docs/35cf91/64891c/dev-notes.md")
        ]
        
        missing_files = []
        for file_path in required_files:
            if not file_path.exists():
                missing_files.append(str(file_path))
        
        assert len(missing_files) == 0, f"项目缺少必要文件: {missing_files}"
        
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists() and docs_dir.is_dir(), "docs目录不存在"
        
        # 检查嵌套目录结构
        nested_dir = Path("docs/35cf91/64891c")
        assert nested_dir.exists() and nested_dir.is_dir(), "文档嵌套目录结构不完整"