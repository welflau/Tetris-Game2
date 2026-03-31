import pytest
from pathlib import Path
from bs4 import BeautifulSoup

class TestIndexHTML:
    
    def setup_method(self):
        """测试前的准备工作，定位HTML文件路径"""
        self.project_root = Path(__file__).parent.parent
        self.html_file = self.project_root / "frontend" / "index.html"
    
    def test_html_file_exists(self):
        """测试HTML文件是否存在"""
        assert self.html_file.exists(), f"HTML文件不存在: {self.html_file}"
        assert self.html_file.is_file(), f"路径不是文件: {self.html_file}"
    
    def test_html_contains_performance_elements(self):
        """测试HTML文件是否包含性能优化相关的关键元素"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否有基本的HTML结构
        assert soup.find('html'), "HTML文件缺少html标签"
        assert soup.find('head'), "HTML文件缺少head标签"
        assert soup.find('body'), "HTML文件缺少body标签"
        
        # 检查性能优化相关元素
        meta_viewport = soup.find('meta', attrs={'name': 'viewport'})
        assert meta_viewport, "缺少viewport meta标签，影响移动端性能"
        
        # 检查是否有CSS或JS引用（性能优化项目应该有）
        css_links = soup.find_all('link', rel='stylesheet')
        script_tags = soup.find_all('script')
        assert len(css_links) > 0 or len(script_tags) > 0, "缺少CSS或JavaScript引用"
    
    def test_html_contains_animation_elements(self):
        """测试HTML文件是否包含动画效果相关的元素或属性"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # 检查是否有动画相关的class或id
        animation_indicators = [
            'animation', 'animate', 'transition', 'transform',
            'fade', 'slide', 'bounce', 'rotate', 'scale'
        ]
        
        found_animation_elements = False
        
        # 检查所有元素的class和id属性
        for element in soup.find_all():
            classes = element.get('class', [])
            element_id = element.get('id', '')
            
            for indicator in animation_indicators:
                if any(indicator.lower() in str(cls).lower() for cls in classes):
                    found_animation_elements = True
                    break
                if indicator.lower() in element_id.lower():
                    found_animation_elements = True
                    break
            
            if found_animation_elements:
                break
        
        # 如果没有找到class/id中的动画标识，检查CSS或JS中是否有动画相关代码
        if not found_animation_elements:
            content_lower = content.lower()
            css_animation_keywords = [
                '@keyframes', 'animation:', 'transition:', 'transform:',
                'requestanimationframe', 'setinterval', 'settimeout'
            ]
            
            for keyword in css_animation_keywords:
                if keyword in content_lower:
                    found_animation_elements = True
                    break
        
        assert found_animation_elements, "HTML文件中未找到动画效果相关的元素或代码"
    
    def test_html_file_size_and_structure(self):
        """测试HTML文件大小合理性和基本结构完整性"""
        # 检查文件大小（性能优化项目应该注意文件大小）
        file_size = self.html_file.stat().st_size
        assert file_size > 100, "HTML文件过小，可能内容不完整"
        assert file_size < 1024 * 1024, "HTML文件过大，可能影响加载性能"
        
        # 检查文件内容结构
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 基本HTML结构检查
        assert '<!DOCTYPE' in content or '<html' in content, "缺少HTML文档类型声明"
        assert '<title>' in content, "缺少页面标题"
        assert content.count('<html') == content.count('</html>'), "HTML标签不匹配"
        assert content.count('<head') == content.count('</head>'), "HEAD标签不匹配"
        assert content.count('<body') == content.count('</body>'), "BODY标签不匹配"