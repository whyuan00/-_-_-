from django.db import models
from django.conf import settings

class Invest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='investments')
    value1 = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    value2 = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    value3 = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    lv = models.IntegerField(null=True, blank=True)  # 최종 성향 레벨
    totalasset = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  # 총 자산
    profit = models.IntegerField(null=True, blank=True)  # 순 수익
    buycount = models.IntegerField(null=True, blank=True)  # 투자 횟수
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜

    def __str__(self):
        return f"{self.user.username} - Investment {self.id}"
