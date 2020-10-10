"""Default queries for reference number building."""
from django.shortcuts import get_object_or_404
from .models import LayerTwoModel, LayerThreeModel, LayerFourModel, LayerFiveModel


class ParentLayerQueryClass:
    """This class holds the methods to query the parents class.

    This class needs to be created to fix the redundant import error of the
    system
    """

    result_list = []

    def insert_empty_value_to_list(self, loop_no=0):
        """Insert value 0 up to the loop no of a list."""
        if loop_no != 0:
            for i in range(loop_no):
                self.result_list.append(0)
        return self.result_list

    def layer_two_query(self, serial_no):
        """Search and make the parent class number."""
        model_obj = get_object_or_404(LayerTwoModel, serial_no=serial_no)
        self.result_list.clear()
        self.result_list.append(model_obj.parent_layer.serial_no)
        self.result_list.append(model_obj.serial_no)
        return self.insert_empty_value_to_list(loop_no=3)

    def layer_three_query(self, serial_no):
        """Search and make the parent class number."""
        model_obj = get_object_or_404(LayerThreeModel, serial_no=serial_no)
        self.result_list.clear()
        self.result_list.append(model_obj.parent_layer.parent_layer.serial_no)
        self.result_list.append(model_obj.parent_layer.serial_no)
        self.result_list.append(model_obj.serial_no)
        return self.insert_empty_value_to_list(loop_no=2)

    def layer_four_query(self, serial_no):
        """Search and make the parent class number."""
        model_obj = get_object_or_404(LayerFourModel, serial_no=serial_no)
        self.result_list.clear()
        self.result_list.append(model_obj.parent_layer.parent_layer.parent_layer.serial_no)
        self.result_list.append(model_obj.parent_layer.parent_layer.serial_no)
        self.result_list.append(model_obj.parent_layer.serial_no)
        self.result_list.append(model_obj.serial_no)
        return self.insert_empty_value_to_list(loop_no=1)

    def layer_five_query(self, serial_no):
        """Search and make the parent class number."""
        model_obj = get_object_or_404(LayerFiveModel, serial_no=serial_no)
        self.result_list.clear()
        self.result_list.append(model_obj.parent_layer.parent_layer.parent_layer.parent_layer.serial_no)
        self.result_list.append(model_obj.parent_layer.parent_layer.parent_layer.serial_no)
        self.result_list.append(model_obj.parent_layer.parent_layer.serial_no)
        self.result_list.append(model_obj.parent_layer.serial_no)
        self.result_list.append(model_obj.serial_no)
        return self.insert_empty_value_to_list()
