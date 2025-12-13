from crewai.tools import BaseTool
from typing import Type, Dict
from pydantic import BaseModel, Field

class AllocateCouponInput(BaseModel):
    merchant_id: str = Field(..., description="ID of merchant giving coupon")
    customer_id: str = Field(..., description="ID of customer receiving coupon")

class AllocateCouponTool(BaseTool):
    name: str = "allocate_coupon_tool"
    description: str = "Allocates a coupon from a merchant to a customer."

    
    args_schema: Type[AllocateCouponInput] = AllocateCouponInput

    def _run(self, merchant_id: str, customer_id: str) -> Dict[str, str]:
        try:
            return {
                "merchant_id": merchant_id,
                "customer_id": customer_id,
                "status": "allocated",
                "message": f"Coupon from {merchant_id} allocated to {customer_id}"
            }
        except Exception as e:
            return {"merchant_id": merchant_id, "customer_id": customer_id, "status": "error", "message": str(e)}
