import numpy as np
import json

def process_matrix(filepath, filepath_save_normalized, filepath_save_json):
  matrix = np.load(filepath)

  total_sum = np.sum(matrix)
  total_avr = np.mean(matrix)

  main_diag_sum = np.trace(matrix)
  main_diag_avr = np.mean(np.diag(matrix))

  side_diag_sum = np.trace(np.fliplr(matrix))
  side_diag_avr = np.mean(np.diag(np.fliplr(matrix)))

  max_val = np.max(matrix)
  min_val = np.min(matrix)

  normalized_matrix = (matrix - min_val) / (max_val - min_val) if max_val != min_val else matrix # Обработка случая, когда все элементы равны

  np.save(filepath_save_normalized, normalized_matrix)


  # Создание JSON-словаря
  result = {
    "sum":int(total_sum),
    "avr": int(total_avr),
    "sumMD": int(main_diag_sum),
    "avrMD": int(main_diag_avr),
    "sumSD": int(side_diag_sum),
    "avrSD": int(side_diag_avr),
    "max": int(max_val),
    "min": int(min_val),
  }
  with open(filepath_save_json, "w") as f:
    json.dump(result, f, indent=4)

if __name__ == '__main__':
  input_file = "./resources/first_task.npy"
  output_matrix_file = "./matrix_normalized.npy"
  output_json_file = "./data.json"
  process_matrix(input_file, output_matrix_file, output_json_file)