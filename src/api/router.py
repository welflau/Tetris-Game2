"""
项目文档编写 - API 路由
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/项目文档编写", tags=["项目文档编写"])


@router.get("")
async def list_项目文档编写():
    """获取列表"""
    return {"items": [], "total": 0}


@router.post("")
async def create_项目文档编写(body: dict):
    """创建"""
    return {"status": "success"}
