# Remote library imports
from faker import Faker

# Local imports
from config import db
from models import User, Report, ReportedPhoto, ReportedFeature

fake = Faker()

def make_report(data):
    # Fetch or create the User
    user_id = data["user_id"]
    user = User.query.filter_by(id=user_id).first()
    if not user:
        # Create a new user using fake data
        user = User(
            id=user_id,
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password()
        )
        db.session.add(user)
        db.session.flush()
    
    # Create the Report instance
    new_report = Report(
        user_id=user.id,
        location_id=data["location_id"],
        comment=data.get("comment", None)
    )
    
    db.session.add(new_report)
    db.session.flush()

    # Prepare the reported photos
    for photo_url in data.get("photo_urls", []):
        new_photos = ReportedPhoto(
            report_id=new_report.id,
            photo_url=photo_url
        )
        db.session.add(new_photos)

    # Prepare the reported features
    for feature_id in data["reported_features_ids"]:
        new_reported_features = ReportedFeature(    
            report_id=new_report.id,
            feature_id=feature_id
        )
        db.session.add(new_reported_features)
        
    db.session.commit()
    return new_report