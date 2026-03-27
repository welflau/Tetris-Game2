"""
开发计划和里程碑制定 - API 路由
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/开发计划和里程碑制定", tags=["开发计划和里程碑制定"])


@router.get("")
async def list_开发计划和里程碑制定():
    """获取列表"""
    return {"items": [], "total": 0}


@router.post("")
async def create_开发计划和里程碑制定(body: dict):
    """创建"""
    return {"status": "success"}
