//
//  Subject.h
//  Qcumber
//
//  Created by Chris Cooper on 11-10-19.
//  Copyright (c) 2011 Chris Cooper. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class Course;

@interface Subject : NSManagedObject {
@private
}
@property (nonatomic, retain) NSString * abbreviation;
@property (nonatomic, retain) NSString * title;
@property (nonatomic, retain) NSSet *courses;

- (void)addCoursesObject:(Course *)value;
- (void)removeCoursesObject:(Course *)value;
- (void)addCourses:(NSSet *)values;
- (void)removeCourses:(NSSet *)values;
@end
