"""
开发里程碑规划 - API 路由
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/开发里程碑规划", tags=["开发里程碑规划"])


@router.get("")
async def list_开发里程碑规划():
    """获取列表"""
    return {"items": [], "total": 0}


@router.post("")
async def create_开发里程碑规划(body: dict):
    """创建"""
    return {"status": "success"}
