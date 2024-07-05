
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
        if operator not in ["==", "!=", ">=", "<=", ">", "<"]:
            raise ValueError(f"Invalid operator: {operator}")

        for field, value in params.items():
            if field in fields_valid:
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
