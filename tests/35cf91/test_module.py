import pytest
from pathlib import Path
import re

class TestProjectStructure:
    """测试投影方块视觉方案项目结构"""
    
    def test_html_file_exists(self):
        """测试主页HTML文件是否存在"""
        html_file = Path("design/index.html")
        assert html_file.exists(), f"HTML文件不存在: {html_file}"
        assert html_file.is_file(), f"路径不是文件: {html_file}"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        dev_notes_file = Path("design/docs/35cf91/e37eae/dev-notes.md")
        assert dev_notes_file.exists(), f"开发文档文件不存在: {dev_notes_file}"
        assert dev_notes_file.is_file(), f"路径不是文件: {dev_notes_file}"
    
    def test_html_contains_projection_elements(self):
        """测试HTML文件包含投影方块相关的关键元素"""
        html_file = Path("design/index.html")
        
        if not html_file.exists():
            pytest.skip("HTML文件不存在，跳过内容测试")
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查基本HTML结构
        assert '<html' in content.lower(), "HTML文件缺少html标签"
        assert '<head>' in content.lower(), "HTML文件缺少head标签"
        assert '<body>' in content.lower(), "HTML文件缺少body标签"
        
        # 检查投影方块相关关键词
        projection_keywords = ['投影', '方块', 'projection', 'cube', 'block']
        content_lower = content.lower()
        found_keywords = [keyword for keyword in projection_keywords if keyword in content_lower]
        assert len(found_keywords) > 0, f"HTML内容中未找到投影方块相关关键词: {projection_keywords}"

class TestDesignModule:
    """测试设计模块功能"""
    
    def test_design_directory_structure(self):
        """测试设计模块目录结构是否正确"""
        design_dir = Path("design")
        assert design_dir.exists(), "design目录不存在"
        assert design_dir.is_dir(), "design路径不是目录"
        
        # 检查docs子目录结构
        docs_dir = design_dir / "docs"
        if docs_dir.exists():
            assert docs_dir.is_dir(), "docs路径不是目录"
    
    def test_html_file_content_structure(self):
        """测试HTML文件内容结构完整性"""
        html_file = Path("design/index.html")
        
        if not html_file.exists():
            pytest.skip("HTML文件不存在，跳过结构测试")
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查DOCTYPE声明
        doctype_pattern = r'<!DOCTYPE\s+html>'
        assert re.search(doctype_pattern, content, re.IGNORECASE), "HTML文件缺少DOCTYPE声明"
        
        # 检查title标签
        title_pattern = r'<title>.*?</title>'
        title_match = re.search(title_pattern, content, re.IGNORECASE | re.DOTALL)
        assert title_match, "HTML文件缺少title标签"
        
        # 检查是否包含CSS或JavaScript引用
        has_css = '<link' in content.lower() or '<style>' in content.lower()
        has_js = '<script' in content.lower()
        assert has_css or has_js, "HTML文件应该包含CSS样式或JavaScript脚本"
    
    def test_dev_notes_content_validity(self):
        """测试开发文档内容有效性"""
        dev_notes_file = Path("design/docs/35cf91/e37eae/dev-notes.md")
        
        if not dev_notes_file.exists():
            pytest.skip("开发文档文件不存在，跳过内容测试")
        
        content = dev_notes_file.read_text(encoding='utf-8')
        
        # 检查Markdown文件不为空
        assert len(content.strip()) > 0, "开发文档文件内容为空"
        
        # 检查是否包含Markdown标记
        markdown_indicators = ['#', '##', '###', '*', '-', '`', '```']
        has_markdown = any(indicator in content for indicator in markdown_indicators)
        assert has_markdown, "开发文档文件应该包含Markdown格式标记"
        
        # 检查是否包含开发相关关键词
        dev_keywords = ['开发', '设计', '方案', '投影', '方块', 'dev', 'design', 'projection']
        content_lower = content.lower()
        found_dev_keywords = [keyword for keyword in dev_keywords if keyword in content_lower]
        assert len(found_dev_keywords) > 0, f"开发文档应该包含相关关键词: {dev_keywords}"