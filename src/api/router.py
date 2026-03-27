"""
技术架构设计文档 - API 路由
"""
from fastapi import APIRouter

router = APIRouter(prefix="/api/技术架构设计文档", tags=["技术架构设计文档"])


@router.get("")
async def list_技术架构设计文档():
    """获取列表"""
    return {"items": [], "total": 0}


@router.post("")
async def create_技术架构设计文档(body: dict):
    """创建"""
    return {"status": "success"}
