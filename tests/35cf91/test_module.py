import pytest
from pathlib import Path
import re

class TestProjectionBlockOutlineStyle:
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_projection_elements(self):
        """测试HTML文件是否包含投影方块相关的关键元素"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含canvas元素或相关的3D渲染容器
        canvas_pattern = r'<canvas|<div[^>]*id[^>]*3d|<div[^>]*class[^>]*render'
        assert re.search(canvas_pattern, content, re.IGNORECASE), "HTML中未找到3D渲染相关元素"
        
        # 检查是否包含样式相关的CSS类或内联样式
        style_pattern = r'outline|border|stroke|line-width'
        assert re.search(style_pattern, content, re.IGNORECASE), "HTML中未找到轮廓线样式相关代码"
    
    def test_html_contains_projection_functionality(self):
        """测试HTML文件是否包含投影功能相关的JavaScript代码或引用"""
        html_file = Path("frontend/index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含JavaScript相关代码
        js_pattern = r'<script|\.js|projection|matrix|transform'
        assert re.search(js_pattern, content, re.IGNORECASE), "HTML中未找到投影功能相关的JavaScript代码"
        
        # 检查是否包含3D相关的库引用或代码
        lib_pattern = r'three\.js|webgl|canvas|perspective|orthographic'
        assert re.search(lib_pattern, content, re.IGNORECASE), "HTML中未找到3D图形库相关引用"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档文件是否存在"""
        notes_file = Path("docs/35cf91/5512df/dev-notes.md")
        assert notes_file.exists(), "开发文档文件不存在"
        assert notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_outline_specifications(self):
        """测试开发文档是否包含轮廓线样式的规格说明"""
        notes_file = Path("docs/35cf91/5512df/dev-notes.md")
        if notes_file.exists():
            content = notes_file.read_text(encoding='utf-8')
            
            # 检查是否包含轮廓线相关的技术说明
            outline_keywords = ['轮廓', 'outline', '边框', 'border', '线条', 'line', '样式', 'style']
            found_keywords = [keyword for keyword in outline_keywords if keyword in content.lower()]
            assert len(found_keywords) > 0, f"开发文档中未找到轮廓线相关关键词: {outline_keywords}"
    
    def test_project_structure_integrity(self):
        """测试项目结构的完整性"""
        frontend_dir = Path("frontend")
        docs_dir = Path("docs/35cf91/5512df")
        
        assert frontend_dir.exists(), "frontend目录不存在"
        assert frontend_dir.is_dir(), "frontend不是一个有效的目录"
        
        assert docs_dir.exists(), "docs目录结构不完整"
        assert docs_dir.is_dir(), "docs路径不是一个有效的目录"
        
        # 检查必要文件
        required_files = [
            Path("frontend/index.html"),
            Path("docs/35cf91/5512df/dev-notes.md")
        ]
        
        for file_path in required_files:
            assert file_path.exists(), f"必要文件缺失: {file_path}"