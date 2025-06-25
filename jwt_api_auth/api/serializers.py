# from .models import student
# from rest_framework import serializers

# class studentregisterserializer(serializers.ModelSerializer):
#     class Meta:
#         model=student
#         fields='__all__'

from rest_framework import serializers
from .models import student,Cource,Stud,Book,Author
from datetime import datetime
# class studentregisterserializer(serializers.ModelSerializer):
#     class Meta:
#         model = student
#         fields = '__all__'

#         def validate_name(self,value):
#             if len(value)>3:
#                 raise serializers.ValidationError("not lesses dhan 3")
#             return value

#         def create(self,validation_data):
#             return student.objects.create(**validation_data)
from rest_framework import serializers
from .models import student

class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

    def validate_name(self, value):
        if 'name' not in value.lower():
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

    def create(self, validated_data):
        return student.objects.create(**validated_data)

class courseregisterserializers(serializers.ModelSerializer):
    class Meta:
        model=Cource
        fields='__all__'



#***********************************


# validation of object validation,field validation validators

def start_with_a(value):
    if value[0].lower() !='a':
        raise serializers.ValidationError("name should be start with r")

class studentserializer(serializers.ModelSerializer):
    name =serializers.CharField(max_length=100,validators=[start_with_a])

    class Meta:
        model = Stud
        fields='__all__'

    def validate_name(self,value):
        if len(value)<3:
            raise serializers.ValidationError("name is less than 3")
        return value
    
    def validate(self,data):
        name=data.get('name')
        roll=data.get('roll')
        if name.lower()=='abhay' and roll<50:
            raise serializers.ValidationError("Data is overloaded: Abhay with age > 50 is not allowed.")
        return data
    


# many to one relation how to coustomise and data to save


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'published_year']

class AuthorSerializer(serializers.ModelSerializer):
    book=serializers.CharField(max_length=220)

class AuthorSerializer(serializers.ModelSerializer):
    book = serializers.CharField(write_only=True)

    class Meta:
        model = Author
        fields = ['name', 'age', 'email','book']

    def create(self, validated_data):
        print(validated_data)
        book_title = validated_data.pop('book') 
        print(book_title)
        author = Author.objects.create(**validated_data)
        print(author)
        if book_title:
            Book.objects.create(author=author, title=book_title,published_year=datetime.now().year)
        return author
    
    # def create(self, validated_data):
    #     book_title = validated_data.pop('book')
    #     author = Author.objects.create(**validated_data)

    #     Book.objects.create(
    #         author=author,
    #         title=book_title,
    #         published_year=datetime.now().year
    #     )
    #     return author
        # def create(self, validated_data):
        #     print(validated_data)
        #     book_title = validated_data.pop('book', None)
        #     print(book_title)
        #     if book_title:
        #         try:
        #             book_instance = Book.objects.get(title=book_title)
        #             print(book_instance)
        #         except Book.DoesNotExist:
        #             raise serializers.ValidationError({"error": "Book does not exist"})
        #     validated_data['book'] = book_instance  
        #     return super().create(validated_data)