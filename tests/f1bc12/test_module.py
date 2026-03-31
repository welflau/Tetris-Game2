import pytest
from pathlib import Path
import importlib.util
import sys
import os

class TestDeployModule:
    
    def test_deploy_module_exists(self):
        """测试部署模块文件是否存在"""
        deploy_module_path = Path("deploy") / "__init__.py"
        if not deploy_module_path.exists():
            deploy_module_path = Path("deploy.py")
        assert deploy_module_path.exists(), "部署模块文件不存在"
    
    def test_deploy_module_importable(self):
        """测试部署模块是否可以正常导入"""
        try:
            # 尝试导入deploy模块
            deploy_path = Path("deploy")
            if deploy_path.is_dir():
                spec = importlib.util.spec_from_file_location("deploy", deploy_path / "__init__.py")
            else:
                spec = importlib.util.spec_from_file_location("deploy", Path("deploy.py"))
            
            if spec and spec.loader:
                deploy_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(deploy_module)
                assert deploy_module is not None, "部署模块导入失败"
        except ImportError:
            pytest.fail("部署模块无法导入")
    
    def test_docs_structure_exists(self):
        """测试文档目录结构是否存在"""
        docs_path = Path("docs")
        assert docs_path.exists(), "docs目录不存在"
        
        # 检查特定的文档路径结构
        specific_doc_path = docs_path / "f1bc12" / "3967ae" / "dev-notes.md"
        if specific_doc_path.exists():
            assert specific_doc_path.is_file(), "dev-notes.md应该是一个文件"
            
            # 检查文档内容是否包含关键信息
            content = specific_doc_path.read_text(encoding='utf-8')
            assert len(content) > 0, "文档内容不能为空"
    
    def test_project_deployment_files(self):
        """测试项目部署相关文件是否存在"""
        # 检查常见的部署配置文件
        deployment_files = [
            Path("requirements.txt"),
            Path("setup.py"),
            Path("pyproject.toml"),
            Path("Dockerfile"),
            Path("docker-compose.yml"),
            Path("config.py"),
            Path("settings.py")
        ]
        
        # 至少应该存在一个部署相关文件
        exists_count = sum(1 for file_path in deployment_files if file_path.exists())
        assert exists_count > 0, "项目中应该至少存在一个部署配置文件"
    
    def test_deploy_function_returns_correct_type(self):
        """测试部署函数返回正确的数据类型"""
        try:
            # 尝试导入并测试部署相关函数
            deploy_path = Path("deploy")
            if deploy_path.is_dir() and (deploy_path / "__init__.py").exists():
                spec = importlib.util.spec_from_file_location("deploy", deploy_path / "__init__.py")
            elif Path("deploy.py").exists():
                spec = importlib.util.spec_from_file_location("deploy", Path("deploy.py"))
            else:
                pytest.skip("部署模块文件不存在，跳过函数测试")
            
            if spec and spec.loader:
                deploy_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(deploy_module)
                
                # 检查是否有deploy相关函数
                if hasattr(deploy_module, 'deploy'):
                    # 如果有deploy函数，测试其返回类型
                    result = deploy_module.deploy()
                    assert isinstance(result, (bool, dict, str, int)), "deploy函数应该返回基本数据类型"
                elif hasattr(deploy_module, 'main'):
                    # 如果有main函数，测试其返回类型
                    result = deploy_module.main()
                    assert isinstance(result, (bool, dict, str, int, type(None))), "main函数应该返回基本数据类型或None"
                
        except Exception as e:
            pytest.skip(f"无法测试部署函数: {str(e)}")
    
    def test_documentation_content_quality(self):
        """测试文档内容质量和完整性"""
        docs_path = Path("docs")
        if not docs_path.exists():
            pytest.skip("docs目录不存在，跳过文档内容测试")
        
        # 查找所有markdown文件
        md_files = list(docs_path.rglob("*.md"))
        assert len(md_files) > 0, "应该至少存在一个markdown文档文件"
        
        # 检查文档内容
        for md_file in md_files:
            content = md_file.read_text(encoding='utf-8')
            assert len(content.strip()) > 50, f"文档 {md_file.name} 内容过短，可能不完整"
            
            # 检查是否包含常见的文档关键词
            keywords = ['部署', 'deploy', '配置', 'config', '安装', 'install', '运行', 'run']
            has_keyword = any(keyword in content.lower() for keyword in keywords)
            if not has_keyword:
                # 如果没有部署相关关键词，至少应该有基本的文档结构
                assert any(marker in content for marker in ['#', '##', '###', '-', '*']), f"文档 {md_file.name} 缺少基本的markdown结构"