extends Sprite

# randomize velocity
# add random rotation speed

var screensize
var extents
var _position
var velocity
var spin

func _ready():
	randomize()
	screensize = get_viewport_rect().size
	extents = get_texture().get_size()/2
	_position = screensize/2
	velocity = Vector2(rand_range(100, 300),0).rotated(rand_range(0,2)*PI)
	spin = rand_range(-PI, PI)
	set_process(true)

func _process(delta):
	set_rotation(get_rotation() + spin * delta)
	_position += velocity * delta
	if _position.x >= screensize.x - extents.x:
		_position.x = screensize.x - extents.x
		velocity.x *= -1
	if _position.x <= 0 + extents.x:
		_position.x = 0 + extents.x
		velocity.x *= -1
	if _position.y >= screensize.y - extents.y:
		_position.y = screensize.y - extents.y
		velocity.y *= -1
	if _position.y <= 0 + extents.y:
		_position.y = 0 + extents.y
		velocity.y *= -1
	set_position(_position)
