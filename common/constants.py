from django.utils.translation import ugettext_lazy as _


error_messages = {
    'first_name' : _('First name can contain only letters.'),
    'last_name' : _('Last name can contain only letters.'),
    'required' : _('This field is required!'),
    'post_title_size' : _('The length of the title can\'t be longer then 200 characters'),
    'no_image' : _('Required. Upload an image!'),
    'full_image_width' : _('The image is %i pixel wide. Needs to be 1920px!'),
    'full_image_height' : _('The image is %i pixel high. Needs to be 1080px!'),
    'medium_image_width' : _('The image is %i pixel wide. Needs to be 750px!'),
    'medium_image_height' : _('The image is %i pixel high. Needs to be 375px!'),
    'small_image_width' : _('The image is %i pixel wide. Needs to be 60px!'),
    'small_image_height' : _('The image is %i pixel high. Needs to be 60px!'),
    'profile_image_width' : _('The image is %i pixel wide. Needs to be 150px!'),
    'profile_image_height' : _('The image is %i pixel high. Needs to be 150px!'),
}

email_activation = {
    'subject' : 'Email activation!',
    'email_sent' : 'We\'ve sent you an email for verification, check your inbox!',
    'link_used' : 'You\'ve already used the activation link, your email is verified!',
    'email_verified' : 'Your email was verified successfuly!',
}

newsletter_texts = {
    'subject' : 'Welcome to our Newsletter',
    'unsubscribe' : 'Sorry to see you go!',
    'email_don\'t_exists' : 'This email address is not subscribed to our system!'
}

help_texts = {
    'email' : _('Required. A valid email (e.g name@example.com).'),
    'only_letters' : _('Required. 100 characters or fewer. Letters only.'),
    'phone_number' : _('Required. prefix + number (e.g. +40123456789).'),
    'date' : _('Required. A valid date (e.g. 2001-04-23), YYYY-MM-DD.'),
    'profile_description' : _('Optional. Letters, digits and/or @/./+/-/_ only.'),
    'obj_name' : _('Required. 100 characters or fewer. Letters, digits and/or @/./+/-/_ only.'),
    'obj_amount' : _('Required. 10 digits or fewer and/or 3 decimals or fewer.'),
    'post_title' : _('Required. 200 characters or fewer. Letters, digits and/or @/./+/-/_ only.'),
    'any_character' : _('Required. Letters, digits and/or special characters.'),
    'full_image' : _('Required. Upload an image with 1920x1080 resolution.'),
    'medium_image' : _('Required. Upload an image with 750x375 resolution.'),
    'small_image' : _('Required. Upload an image with 60x60 resolution.'),
}

messages_text = {
    'email_exists' : 'This email is already subscribed in our system!',
    'email_subscribed' : 'Your email was subscribed in our system, you\'ll hear from us as soon as possible!',
    'email_received' : 'We\'ve received your email, you\'ll hear from us very soon!',
    'fail_sent_email' : 'Something didn\'t work, please try later!',
    'profile_updated' : 'Your profile was updated successfully',
}

template_titles = {
    'blog_title' : 'Blog',
    'blog_path' : 'home / blog',
    'post_title' : 'Post',
    'post_create' : 'Add Post',
    'post_update' : 'Update Post',
    'post_path' : 'home / post',
    'no_previous_post' : 'No previous post',
    'no_next_post' : 'No next post',
    'about_title' : 'About Us',
    'about_path' : 'home / about',
    'contact_title' : 'Contact',
    'contact_path' : 'home / contact',
    'dashboard_title' : 'Dashboard',
    'incomes_title' : 'Incomes',
    'spendings_title' : 'Spendings',
    'profile_title' : 'Profile',
    'archive_title' : 'Archive',
    'terms_and_conditions_title' : 'Terms & Conditions',
    'terms_and_conditions_path' : 'home / terms-and-conditions',
    'privacy_policy_title' : 'Privacy Policy',
    'privacy_policy_path' : 'home / privacy-policy',
}
