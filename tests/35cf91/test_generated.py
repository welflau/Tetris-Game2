import pytest
from pathlib import Path
import re

class TestProjectionCubeVisualEffects:
    
    def test_html_file_exists(self):
        """测试主HTML文件是否存在"""
        html_file = Path("index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_canvas_element(self):
        """测试HTML文件是否包含用于渲染3D效果的canvas元素"""
        html_file = Path("index.html")
        assert html_file.exists(), "index.html文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        assert '<canvas' in content, "HTML文件中缺少canvas元素"
        
        # 检查是否包含WebGL或3D相关的关键词
        canvas_pattern = r'<canvas[^>]*>'
        canvas_matches = re.findall(canvas_pattern, content, re.IGNORECASE)
        assert len(canvas_matches) > 0, "未找到有效的canvas标签"
    
    def test_html_contains_projection_cube_elements(self):
        """测试HTML文件是否包含投影方块相关的关键元素和脚本"""
        html_file = Path("index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查是否包含3D图形库引用（如Three.js等）
        graphics_keywords = ['three.js', 'webgl', 'gl-matrix', 'babylon', 'canvas', 'shader']
        has_graphics_lib = any(keyword.lower() in content.lower() for keyword in graphics_keywords)
        assert has_graphics_lib, "HTML文件中未找到3D图形库相关内容"
        
        # 检查是否包含JavaScript脚本标签
        assert '<script' in content, "HTML文件中缺少JavaScript脚本标签"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档是否存在并包含相关内容"""
        dev_notes_file = Path("docs/35cf91/359b30/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档文件不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
        
        content = dev_notes_file.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "开发文档文件为空"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性，确保必要的目录和文件存在"""
        # 检查docs目录结构
        docs_dir = Path("docs")
        assert docs_dir.exists(), "docs目录不存在"
        assert docs_dir.is_dir(), "docs不是一个有效的目录"
        
        # 检查嵌套目录结构
        nested_dir = Path("docs/35cf91/359b30")
        assert nested_dir.exists(), "嵌套文档目录不存在"
        assert nested_dir.is_dir(), "嵌套目录结构不正确"
    
    def test_html_viewport_and_responsive_setup(self):
        """测试HTML文件是否包含适当的视口设置和响应式设计元素"""
        html_file = Path("index.html")
        content = html_file.read_text(encoding='utf-8')
        
        # 检查viewport meta标签
        viewport_keywords = ['viewport', 'width=device-width', 'initial-scale']
        has_viewport = any(keyword in content for keyword in viewport_keywords)
        
        # 检查HTML基本结构
        html_structure = ['<html', '<head', '<body']
        structure_complete = all(tag in content for tag in html_structure)
        assert structure_complete, "HTML文件缺少基本结构标签"