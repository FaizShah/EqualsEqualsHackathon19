class Food < ApplicationRecord
  mount_base64_uploader :image, FoodImageUploader


end
