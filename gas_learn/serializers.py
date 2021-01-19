from rest_framework import serializers
from .models import BlockInfo, BlockCateInfo, MpoolInfo, MpoolCateInfo

class BlockCateSerializer(serializers.ModelSerializer):

    """
    block cate info
    """

    class Meta:
        model = BlockCateInfo
        fields = '__all__'

class BlockSerializer(serializers.ModelSerializer):

    """
    block
    """

    cates = BlockCateSerializer(many=True)

    class Meta:
        model = BlockInfo
        fields = ['id', 'epoch', 'created', 'block_count', 'basefee', 'cates']

    def create(self, validated_data):
        cates_data = validated_data.pop('cates')
        block_info = BlockInfo.objects.create(**validated_data)
        for cate_data in cates_data:
            BlockCateInfo.objects.create(foreign=block_info, **cate_data)
        return block_info

class MpoolCateSerializer(serializers.ModelSerializer):

    """
    mpool cate info
    """

    class Meta:
        model = MpoolCateInfo
        fields = '__all__'

class MpoolSerializer(serializers.ModelSerializer):

    """
    mpool
    """

    cates = MpoolCateSerializer(many=True)

    class Meta:
        model = MpoolInfo
        fields = ['created', 'epoch', 'cates']

    def create(self, validated_data):
        cates_data = validated_data.pop('cates')
        mpool_infos = MpoolInfo.objects.create(**validated_data)
        for cate_data in cates_data:
            MpoolCateInfo.objects.create(foreign=mpool_infos, **cate_data)
        return mpool_infos