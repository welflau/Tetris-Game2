import pytest
from pathlib import Path
import re

class TestProjectionCubeVisualEffects:
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        html_file = Path("index.html")
        assert html_file.exists(), "index.html文件不存在"
        assert html_file.is_file(), "index.html不是一个有效的文件"
    
    def test_html_contains_canvas_element(self):
        """测试HTML文件是否包含用于渲染3D投影方块的canvas元素"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8')
        assert '<canvas' in content, "HTML文件中缺少canvas元素"
        assert 'id=' in content or 'class=' in content, "canvas元素缺少标识符"
    
    def test_html_contains_webgl_or_3d_keywords(self):
        """测试HTML文件是否包含WebGL或3D相关的关键词，确保支持投影方块渲染"""
        html_file = Path("index.html")
        assert html_file.exists(), "HTML文件不存在"
        
        content = html_file.read_text(encoding='utf-8').lower()
        webgl_keywords = ['webgl', 'three.js', 'threejs', 'gl-matrix', 'babylon', 'canvas', '3d']
        
        has_3d_support = any(keyword in content for keyword in webgl_keywords)
        assert has_3d_support, f"HTML文件中未找到3D渲染相关关键词: {webgl_keywords}"
    
    def test_dev_notes_file_exists(self):
        """测试开发文档是否存在"""
        dev_notes_file = Path("docs/35cf91/359b30/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档dev-notes.md不存在"
        assert dev_notes_file.is_file(), "dev-notes.md不是一个有效的文件"
    
    def test_dev_notes_contains_project_info(self):
        """测试开发文档是否包含项目相关信息和技术说明"""
        dev_notes_file = Path("docs/35cf91/359b30/dev-notes.md")
        assert dev_notes_file.exists(), "开发文档不存在"
        
        content = dev_notes_file.read_text(encoding='utf-8').lower()
        project_keywords = ['投影', '方块', '视觉', '效果', 'projection', 'cube', 'visual', 'effect']
        
        has_project_info = any(keyword in content for keyword in project_keywords)
        assert has_project_info, f"开发文档中未找到项目相关关键词: {project_keywords}"
    
    def test_project_structure_integrity(self):
        """测试项目结构完整性，确保核心文件都存在"""
        required_files = [
            Path("index.html"),
            Path("docs/35cf91/359b30/dev-notes.md")
        ]
        
        missing_files = []
        for file_path in required_files:
            if not file_path.exists():
                missing_files.append(str(file_path))
        
        assert len(missing_files) == 0, f"缺少必要的项目文件: {missing_files}"
        
        # 检查docs目录结构
        docs_dir = Path("docs/35cf91/359b30")
        assert docs_dir.exists(), "docs目录结构不完整"
        assert docs_dir.is_dir(), "docs路径不是目录"