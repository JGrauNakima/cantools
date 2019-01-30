# A CAN environmental variable.

class EnvironmentalVariable(object):
    """A CAN environmental variable.

    """

    def __init__(self,
                 name,
                 type,
                 minimum,
                 maximum,
                 unit,
                 initial_value,
                 id,
                 access_type,
                 access_node,
                 comment):
        self._name = name
        self._type = type
        self._minimum = minimum
        self._maximum = maximum
        self._unit = unit
        self._initial_value = initial_value
        self._id = id
        self._access_type = access_type
        self._access_node = access_node
        self._comment = comment

    @property
    def name(self):
        """The environmental variable name as a string.

        """

        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        """The environmental variable type as a string.

        """

        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def minimum(self):
        """The environmental variable minimum as a string.

        """

        return self._minimum

    @minimum.setter
    def minimum(self, value):
        self._minimum = value

    @property
    def maximum(self):
        """The environmental variable maximum as a string.

        """

        return self._maximum

    @maximum.setter
    def maximum(self, value):
        self._maximum = value

    @property
    def unit(self):
        """The environmental variable unit as a string.

        """

        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    @property
    def initial_value(self):
        """The environmental variable initial_value as a string.

        """

        return self._initial_value

    @initial_value.setter
    def initial_value(self, value):
        self._initial_value = value

    @property
    def id(self):
        """The environmental variable id as a string.

        """

        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def access_type(self):
        """The environmental variable access_type as a string.

        """

        return self._access_type

    @access_type.setter
    def access_type(self, value):
        self._access_type = value

    @property
    def access_node(self):
        """The environmental variable access_node as a string.

        """

        return self._access_node

    @access_node.setter
    def access_node(self, value):
        self._access_node = value

    @property
    def comment(self):
        """The node comment, or ``None`` if unavailable.

        """

        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    def __repr__(self):
        return "environmental_variable('{}', {}, {}, {}, '{}', {}, {}, '{}', '{}', {})".format(
            self._name,
            self._type,
            self._minimum,
            self._maximum,
            self._unit,
            self._initial_value,
            self._id,
            self._access_type,
            self._access_node,
            "'" + self._comment + "'" if self._comment is not None else None)
