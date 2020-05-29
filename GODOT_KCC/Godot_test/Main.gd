extends Node2D

#Variables
onready var sprite = preload("res://Sprite.tscn") # res stands for resource

func _ready():
	for i in range(1000):
		var spriteInstance = sprite.instance()
		add_child(spriteInstance)
