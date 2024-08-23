
class FilterParamsFieldModels:

    def filter_belong_model(self, model, params: dict) -> dict:
        """
        Filters valid field names from the provided params based on the model's attributes.

        Args:
            model: The SQLAlchemy model class.
            params: A dictionary containing filter parameters.

        Returns:
            A dictionary containing valid field names as keys and True values.
        """
        names_valid = {field: True for field in params if getattr(model, field)}
        return names_valid

    def filter_format(self, model, params: dict, operator: str = "==") -> list:
        """
        Generates SQLAlchemy filters based on the provided params and operator.

        Args:
        model: The SQLAlchemy model class.
        params: A dictionary containing filter parameters.
        operator: The comparison operator to use (default: ==").

        Returns:
        A list of SQLAlchemy filter expressions.

        Raises:
        ValueError: If an invalid operator is provided.
        """
        filters = []
        fields_valid = self.filter_belong_model(model, params)
        self.operator_valid(operator)

        for field, value_field in params.items():
            if field in fields_valid:

                #It is possible to pass a value with two parameters, the value and the operator into a list
                customs = self.handle_custom_parameter(value_field)
                if len(customs)>1 and self.operator_valid(customs[0]):                    
                    value = customs[1]
                    operator = customs[0]
                else:
                    value = value_field

                if operator == "==":
                    filters.append(getattr(model, field) == value)
                elif operator == "!=":
                    filters.append(getattr(model, field) != value)
                elif operator == ">=":
                    filters.append(getattr(model, field) >= value)
                elif operator == "<=":
                    filters.append(getattr(model, field) <= value)
                elif operator == ">":
                    filters.append(getattr(model, field) > value)
                elif operator == "<":
                    filters.append(getattr(model, field) < value)
        return filters

    def operator_valid(self, operator: str):
        if operator not in ["==", "!=", ">=", "<=", ">", "<"]:
            raise ValueError(f"Invalid operator: {operator}")            
        return True
        
    def handle_custom_parameter(self, value: str):
        content = value.split("&")
        return content