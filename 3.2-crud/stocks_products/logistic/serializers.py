from rest_framework import serializers
from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']
    # настройте сериализатор для продукта


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'address']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = StockProduct
        fields = ['positions', 'quantity', 'price']

    # настройте сериализатор для склада
    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        print(validated_data)
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(**validated_data)
        StockProduct.objects.create(stock=stock, **positions)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
